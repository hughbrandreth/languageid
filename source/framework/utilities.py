import string
import numpy
import pandas

# This file contains functions that may be used by all classes
# and functions in the system and therefore need to be
# accessible everywhere


#########################################################
###### not sure whether this is needed any more #########

#A function which extracts all possible ngrams of a word
def Ngrams(Word):

    Result = []

    for i in range(len(Word)):
        for j in range(len(Word) - i):
            Result.append(Word[i: i + j + 1])

    return Result

#a function which extracts all possible ngrams, and returns them uniqely
def UniqueNgrams(Word):
    return set(Ngrams(Word))
#########################################################



#A function which extracts all possible ngrams of a word with parameterisable ngram lengths
def MinLengthNgrams(Word, MinLength):
    '''
    This function determines all possible substrings of a word and adds them to a list.
    The minimum length a substring can be is a parameter.

    :param str Word:
    :param int MinLength:
    :return: list of strings
    '''
    Result = []

    for i in range(len(Word)):
        for j in range(MinLength - 1, len(Word) - i):
            Result.append(Word[i: i + j + 1])

    return Result

#a function which extracts all possible minlengthngrams, and returns them uniqely
def UniqueMinLengthNgrams(Word, MinLength):
    '''Eliminates duplicates from the result of MinLengthNgrams'''
    return set(MinLengthNgrams(Word, MinLength))

FullLangList = [
'ar','bn','bg','ca','zh','cs','da','nl','en','fi','fr','de','el','he','hi','hu','is','id','it','ja','ko','lv','lt','mk','ms','nb','fa','pl','pt','ro','ru','sh','sl','sk','es','sv','fil','ta','tr','uk','ur','vi'
]


def StripString(RawString):
    PunctuationString = "!\"#$%&'()*+, -./:;<=>?@[\]^_`{|}~£"
    return RawString.translate(str.maketrans("", "", PunctuationString))


def ConstructDataFrame(self, data, Rows, Columns):
    DataFrame = pandas.Dataframe(data, Rows, Columns)
    return DataFrame


def FindLetterFreqs(WordList, WordFreqList):
    '''
    This function takes every word in the list and calculates the frequency of occurrence of each character in the list.
    It then calculates the probability of the characters by dividing their frequencies by the total sum.
    It ignores any characters which are not lowercase letters.

    :param list WordList:
    :param list WordFreqList:
    :return: numpy array of floats between 0 and 1
    '''
    LetterFreqArray = numpy.zeros(26)
    for Word, WordFreq in zip(WordList, WordFreqList):
        for Character in Word:
            Ordinal = ord(Character) - 97
            if Ordinal <= 25 and Ordinal >= 0:
                LetterFreqArray[Ordinal] += WordFreq
    Sum = numpy.sum(LetterFreqArray)
    return numpy.vectorize(lambda Freq: Freq / Sum)(LetterFreqArray)

