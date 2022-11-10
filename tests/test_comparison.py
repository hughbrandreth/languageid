import pytest
from aug22.source.framework.Comparison import *
from aug22.source.framework.Language import Language
from aug22.source.framework.Text import Text

def test_GetPerfectMatchScore1():
    English = Language("wordfreq", "en")
    TestComp1 = Comparison(Text("en#the cat sat on the mat", r"the/moon"), English)
    assert TestComp1.Text.SuccessfullyInitialised
    #assert TestComp1.PerfectMatch() == 1.0
    return

def test_GetPerfectMatchScore2():
    English = Language("wordfreq", "en")
    TestComp2 = Comparison(Text("en#the cat sat on xat", r"the/moon"), English)
    assert TestComp2.PerfectMatch() == 0.8
    return

def test_GetPerfectMatchScore3():
    English = Language("wordfreq", "en")
    TestComp3 = Comparison(Text("en#orjdgodgoisgjolwaji iiiiiiiiigaowijgoeghoihw owwfigh afewafe owhe fowjijw ", r"the/moon"), English)
    assert TestComp3.PerfectMatch() == 0.0
    return

def test_LevenshteinScore1():
    English = Language("wordfreq", "en")
    TestComp1 = Comparison(Text("en#the cat sat on the mat", r"the/moon"), English)
    assert TestComp1.LevenshteinMatch() == 1.0
    return

def test_LevenshteinScore2():
    English = Language("wordfreq", "en")
    TestComp2 = Comparison(Text("en#the ctat sat on the mat", r"the/moon"), English)
    assert TestComp2.LevenshteinMatch() == 23/24    #average of 1xthe number of perfect matches and 3/4 for "ctat" is 23/24. This should be the Levenshtein match as "ctat" is a distance of 1 from "chat".
    return

def test_LevenshteinScore3():
    English = Language("wordfreq", "en")
    TestComp3 = Comparison(Text("en#the ctat iat on the double lever rentrer pilot piscine mat", r"the/moon"), English)
    ##### There are four words here which are not standard English words.

    assert abs(TestComp3.LevenshteinMatch() - (43 / 48)) < 0.01 # Rounding makes a slight error
    assert TestComp3.SuccessfullyInitialised
    return

def test_LevenshteinScore4():
    English = Language("wordfreq", "en")
    assert English.SuccessfullyInitialised
    French = Language("wordfreq", "fr")
    SampleEnglishText = Text("en#", "the_back_of_a_penguin_bar")
    assert not SampleEnglishText.SuccessfullyInitialised
    TestComp = Comparison(SampleEnglishText, English)
    assert not TestComp.SuccessfullyInitialised
    return
