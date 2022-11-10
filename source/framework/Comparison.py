import aug22.source.framework.Text
import aug22.source.framework.Language
import time
import Levenshtein
import numpy
from aug22.source.Timelogger import Timelogger
from aug22.source.framework.utilities import *
#future additions: speech recognition, hashing ngrams similar to words in Language to increase speed, look at how much lenience affects relative results
# iterate through increasingly vague sets of ngrams
# possibility of applying logic to Text or to Language
# quality vs time analysis
# analyse results of various lanugage and deducing things
# do preliminary analysis to determine order (which Language do i pick first)
# runtime vs quality of results as parameters
# comparing algorithms on test corpora
# compare performances of Languages in real time simultaneously
# letter frequencies as preliminary analysis
# train with a nn

from statistics import mean


class Comparison:

    def __init__(self, ThisText, ThisLanguage):

        self.SuccessfullyInitialised = True

        if not ThisText.SuccessfullyInitialised:
            self.SuccessfullyInitialised = False
            return

        if not ThisLanguage.SuccessfullyInitialised:
            self.SuccessfullyInitialised = False
            return


        self.Text = ThisText
        self.Language = ThisLanguage

        self.TextSet = self.Text.WordSet
        self.LanguageSet = self.Language.WordSet

        self.PerfectMatchScore = 0
        self.SubstringMatchScore = 0
        self.LevenshteinMatchScore = 0
        self.HammingMatchScore = 0
        self.HammingMatchScoreList = []

        self.Timetaken = 0


    def CheckInitiation(self):
        return self.SuccessfullyInitialised


    @Timelogger
    def PerfectMatch(self):
        '''
        String matching algorithm for computing the similarity of a text and a language.
        Checks to see whether each word is in the language, and gives a score of 1 for true and 0 for false.
        The average is then computed. This is equal to the proportion of words in the text which can be found in the language

        :return: Float from 0 -> 1

        '''

        PerfectMatchCount = 0
        for Word in self.TextSet:
            if self.Language.ContainsWord(Word):
                PerfectMatchCount += 1

        self.PerfectMatchScore = PerfectMatchCount / len(self.TextSet)
        return self.PerfectMatchScore


    def FindBestLevenshtein(self, Word):
        if self.Language.ContainsWord(Word):
            return 0
        else:
            WordLength = len(Word)
            BestScore = WordLength
            for LangWord in filter(lambda w: abs(len(w)-WordLength) <= 1, self.Language.WordSet):
                BestScore = min(Levenshtein.distance(Word, LangWord), BestScore)
                ### The Best Possible Levenshtein Score is zero, for words that are identical. Since these words are NOT identical, the best possible score is 1, and therefore
                ### it is not worth continuing
                if BestScore == 1:
                    return BestScore / WordLength

            return BestScore / WordLength


    @Timelogger
    def LevenshteinMatch(self):
        '''
        For every word in the text, this algorithm computes the lowest possible Levenshtein distance between this word and every word in the language.
        It first checks whether the word is actually in the language already, since in this case it would have a distance of zero.
        The score is normalised to be between 0 and 1 and inverted.
        The mean of all these scores in the text is then computed.

        :return: Float from 0 -> 1
        '''
        if len(self.Text.Words) > 0:
            return 1 - mean(map(self.FindBestLevenshtein, self.Text.Words))
        else:
            return 0


    @Timelogger
    def HammingMatch(self):
        '''
        For every word in the text, this algorithm computes the lowest possible Hamming distance between this word and every word in the language.
        It first checks whether the word is actually in the language already, since in this case it would have a distance of zero.
        The score is normalised to be between 0 and 1 and inverted.
        The mean of all these scores in the text is then computed.

        :return: Float from 0 -> 1
        '''

        #This computes the ratio as well, but using the hamming algorithm on the whole strings using an inbuilt package
        HammingScoreList = []
        for Word in self.Text.Words:
            if Word in self.Language.WordSet:
                HammingScoreList.append(0)
            else:
                WordLength = len(Word)
                LangWordsOfSameLength = list(filter(lambda x: len(x) == WordLength, self.Language.WordSet))
                if len(LangWordsOfSameLength) == 0:
                    HammingScoreList.append(0)
                else:
                    HammingScoreList.append((WordLength - min(map(lambda x: Levenshtein.hamming(x, Word), LangWordsOfSameLength))) / WordLength)
                ##### Opportunity for optimisation by early termination -- algorithm should give up after a match that can't be beaten.
        return 1 - mean(HammingScoreList)



    def MeanWordFreq(self):
        if len(self.Text.Words) > 0:
            return mean(map(lambda word: self.Language.GetFreq(word), self.Text.Words))
        else:
            return 0

    @Timelogger
    def SubStringMatch(self):
        '''
        String matching algorithm for computing the similarity of a text and a language.
        Finds the best match between strings by finding the words in the language with the largest possible common substring with each word in the text,
        and selecting the word in the language out of those which is most similar in length to the word in the text.
        Computes an average score normalised between nought and one.

        :return: Float from 0 -> 1
        '''

        TotalScore = 0.0
        for Word in self.Text.Words:
            if self.Language.ContainsWord(Word):
                RunningScore = len(Word)
            else:
                RunningScore = 0
                for Ngram in UniqueMinLengthNgrams(Word, 3):
                    for Match in self.Language.WordsContainingNgram(Ngram):

                        if (len(Ngram) / (abs(len(Match) - len(Word)) + 1)) > RunningScore:
                            RunningScore = (len(Ngram) / (abs(len(Match) - len(Word)) + 1))
            TotalScore = TotalScore + RunningScore/len(Word)

        self.SubstringMatchScore = TotalScore/len(self.Text.Words)
        return self.SubstringMatchScore


    def PerfectMatchOnFirstnWords(self, NumberofWords):
        '''
        This is identical to the PerfectMatch algorithm, except in that it only looks for matches for a certain portion of the text, specified in the input.

        :param int NumberofWords:
        :return: Score as float 0 -> 1
        '''
        PerfectMatchCount = 0
        for Word in self.Text.Words[:NumberofWords]:
            if self.Language.ContainsWord(Word):
                PerfectMatchCount += 1

        return PerfectMatchCount / len(self.Text.Words[:NumberofWords])

    @Timelogger
    def PerfectMatchOnFirst5Words(self):
        return self.PerfectMatchOnFirstnWords(5)

    @Timelogger
    def PerfectMatchOnFirst10Words(self):
        return self.PerfectMatchOnFirstnWords(10)

    @Timelogger
    def PerfectMatchOnFirst20Words(self):
        return self.PerfectMatchOnFirstnWords(20)

    @Timelogger
    def LetterFreqComp(self):
        '''
        Compares the relative frequency of all of the letters of the alphabet in the text and the language.
        It does this by considering the 26 frequencies as a vector, and computing the vector distance
        between the two. It takes no parameters.

        :return:Float from 0 -> 1
        '''
        return 1 - numpy.linalg.norm(self.Text.GetLetterFreqs() - self.Language.GetLetterFreqs())

    def GetTimetaken(self):     ### not used
        return self.Timetaken



