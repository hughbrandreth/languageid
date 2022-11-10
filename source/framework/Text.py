from aug22.source.Timelogger import Timelogger
import numpy

from aug22.source.framework.utilities import FindLetterFreqs, FullLangList


class Text:

    def __init__(self, Line, Source):

        #setting up
        self.Key = ''

        self.SuccessfullyInitialised = True
        if type(Line) != str:
            self.SuccessfullyInitialised = False
        if type(Source) != str:
            self.SuccessfullyInitialised = False

        if self.SuccessfullyInitialised:

            self.Source = Source
            self.SourceDir = r"E:/Hugh/HDD Documents/Python Programs/Decipheronator/source/sampletexts/" + Source
            self.LangKnown = False
            self.LetterFreqArray = None

            #obtaining Language from start of line: this is separated by a % char.
            LangSeparatedLine = Line.split("#")
            if len(LangSeparatedLine) == 2 and LangSeparatedLine[0] in FullLangList:
                self.LangKnown = True
                self.Lang = LangSeparatedLine[0]

            else:
                self.LangKnown = False  # I know this is redundant - it is just for clarity.
                self.Lang = "??"        ###### If we dont find a text at all, we can't do anything. This else statement prevents a crash if the expected structure is not found.

            self.Content = LangSeparatedLine[1]
            self.Words = self.Content.split()

            if len(self.Words) == 0:
                self.SuccessfullyInitialised = False
                return

            self.WordSet = set(self.Words)
            self.Length = len(self.Words)
            return

        else:
            return

    ##### OUTPUT FUNCTIONS #####

    def CheckInitiation(self):
        return self.SuccessfullyInitialised

    def ContainsWord(self, Word):
        if self.SuccessfullyInitialised:
            return (Word in self.Words) #returns boolean
        else:
            return False

    def GetCount(self, Word):
        #return len([w for w in self.Words if w == Word]) #returns int giving word Count
        if self.SuccessfullyInitialised:
            return self.Words.count(Word)
        else:
            return 0

    def GetLength(self):
        return self.Length

    def Freq(self, Word):
        '''
        What proportion of the piece of text is comprised of this word?
        i.e. how common is the word
        '''
        return self.GetCount(Word) / self.GetLength()

    def GetLetterFreqs(self):
        '''
        Obtains the relative frequencies of all of the letters.
        If they have not been generated then this is requested.

        :return: numpy array of floats between 0 and 1.
        '''

        if self.SuccessfullyInitialised:
            if self.LetterFreqArray is None:
                self.LetterFreqArray = FindLetterFreqs(self.Words, [1] * self.Length)
            return self.LetterFreqArray
        else:
            return None


