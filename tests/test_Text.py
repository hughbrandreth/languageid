from aug22.source.framework.Text import *

# A case designed to behave as we expect the class to behave, by providing typical inputs.
def test_TextExpectedCase():
    TestText = Text("is#to be or not to be that is the question", "back_of_an_envelope")
    assert TestText.SuccessfullyInitialised
    assert TestText.Words[0] == "to"
    assert len(TestText.Words) == 10
    assert len(TestText.WordSet) == 8 #This is the number of unique words in the text.
    assert not TestText.ContainsWord("hypersonic")
    assert TestText.ContainsWord("that")
    assert TestText.GetCount("be") == 2
    assert TestText.GetCount("") == 0
    assert TestText.GetCount("porcupine") == 0
    assert TestText.Freq("be") == 1/5
    assert TestText.Freq("question") == 1/10
    assert TestText.Freq("misanthrope") == 0
    assert TestText.GetLetterFreqs()[0] == 1/30
    assert TestText.LetterFreqArray[25] == 0.0
    return

def test_TextUnusualInputs():

    TestText = Text("gibberishese#mary had a little lamb", "downthebackofthesofa")
    assert TestText.SuccessfullyInitialised
    assert not TestText.LangKnown

    return

# A case where unexpected inputs are provided
def test_TextWrongFormatInputs():

    TestText = Text("gibberishese#the cat sat on the mat", 1)
    assert not TestText.SuccessfullyInitialised

    return