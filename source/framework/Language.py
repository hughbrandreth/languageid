from wordfreq import *
from aug22.source.framework.utilities import *


class Language:

    def __init__(self, SourceType, InputName):

        self.SuccessfullyInitialised = True
        if SourceType != "corpus" and SourceType != "wordfreq":
            self.SuccessfullyInitialised = False
        if SourceType == "wordfreq" and InputName not in available_languages():
            self.SuccessfullyInitialised = False

        if not self.SuccessfullyInitialised:
            return

        #setting up
        self.Source = InputName
        self.WordSet = set()
        self.WordFreqDict = {}
        self.LetterFreqArray = None

        #check where we are getting our data from:
        if SourceType == "corpus":
            #if we are reading from a corpus, the corpus must be read and the frequencies of words must be extracted:
            #extracting Text from file
            File = open(InputName, 'r', encoding = 'utf-8')

            WordCounts = {}
            TotalWordCount = 0

            for Line in File.readlines():
                for Word in Line.split():
                    if not Word in self.WordSet:
                        self.WordSet.add(Word)
                        WordCounts[Word] = 1
                    else:
                        WordCounts.update({Word: WordCounts[Word] + 1})
                    TotalWordCount += 1

            File.close()

            for Word, Count in WordCounts.items():
                self.WordFreqDict[Word] = Count / TotalWordCount



        elif SourceType == "wordfreq":
            #if we are reading from the python wordfreq package, we will need to read in all of its data
            self.WordFreqDict = get_frequency_dict(InputName, "small")
            self.WordSet = set(self.WordFreqDict.keys())


        self.NgramDict = dict()
        for Word in self.WordFreqDict.keys():
            for Ngram in UniqueNgrams(Word):
                if not Ngram in self.NgramDict:
                    self.NgramDict[Ngram] = {Word}
                else:
                    self.NgramDict[Ngram].add(Word)




# Internal Functions

    def CheckInitiation(self):
        return self.SuccessfullyInitialised

    def FindLetterFreqs(self):
        """
        Calculates the relative frequencies of the letters in the text. This is saved so that it does not have to be computed several times.
        It takes no parameters.
        :return: None
        """

        if not self.SuccessfullyInitialised:
            return
        else:
            self.LetterFreqArray = FindLetterFreqs(list(self.WordFreqDict.keys()), list(self.WordFreqDict.values()))
        return


# Output functions

    def ContainsWord(self, Word):
        '''
        Checks whether a word is in the dictionary
        :return: bool
        '''

        if not self.SuccessfullyInitialised:
            return False
        else:
            return (Word in self.WordFreqDict)

    def GetFreq(self, Word):
        '''Finds the frequency of the word in the language from the dictionary'''

        if not self.SuccessfullyInitialised:
            return 0

        elif Word in self.WordFreqDict:
            return self.WordFreqDict[Word] #returns int giving word Count
        else:
            return 0 #not being in the dictionary is equivalent to a frequency of zero

    def WordsContainingNgram(self, Ngram):
        '''
        This function obtains from a dictionary a set of words which contain the string supplied to it.
        If the string does not appear in the dictionary then no words contain it and the function therefore returns an empty set.
        :param Ngram:
        :return: set of words as strings or empty set
        '''

        if not self.SuccessfullyInitialised:
            return {}

        elif Ngram in self.NgramDict:
            return self.NgramDict[Ngram]
        else:
            return {}


    def GetLetterFreqs(self):
        '''
        This returns the letter frequencies and generates them if they have not already been generated.

        :return: numpy array of floats between 0 and 1
        '''

        if not self.SuccessfullyInitialised:
            return None

        elif self.LetterFreqArray is None:
            self.__FindLetterFreqs()
        return self.LetterFreqArray