from aug22.source.framework.Language import *

def test_Language_Initialisation():
    TestLanguage = Language("wordfreq", "en")
    assert TestLanguage.SuccessfullyInitialised
    return

def test_Language_Initialisation2():
    TestLanguage = Language("wordfreq", "unexpectedstring")
    assert not TestLanguage.SuccessfullyInitialised
    return

def test_Language():
    TestLanguage = Language("wordfreq", "en")
    TestLanguage.FindLetterFreqs()
    ##### We should see that in the English Language, the letter "T" is more common than the letter "V". If our system is functioning properly, it should reflect this.
    assert TestLanguage.LetterFreqArray[19] > TestLanguage.LetterFreqArray[21]
    return

def test_Language_ContainsWord():
    TestLanguage = Language("wordfreq", "en")
    assert TestLanguage.ContainsWord("penguin")
    return

def test_Language_WordsContainingNgram():
    TestLanguage = Language("wordfreq", "en")
    assert len(TestLanguage.WordsContainingNgram("trhrshrshrsthsrthrsh")) == 0
    assert len(TestLanguage.WordsContainingNgram("")) == 0
    return

def test_Language_Uninitialised():
    TestLanguage = Language("wordfreq", "pig_latin")
    assert not TestLanguage.SuccessfullyInitialised
    assert not TestLanguage.ContainsWord("cannonball")
    assert TestLanguage.GetFreq("rhinoceros") == 0
    return

def test_Language_GetFreq():
    TestLanguage = Language("wordfreq", "en")
    assert TestLanguage.GetFreq("the") > 0.00001
    assert TestLanguage.GetFreq("blimble") == 0
    return

