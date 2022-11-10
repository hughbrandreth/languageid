from aug22.source.framework.utilities import *


def test_Ngrams():
    assert len(Ngrams("a")) == 1
    assert len(Ngrams("")) == 0
    assert len(Ngrams("aaaa")) == 10
    return

def test_UniqueNgrams():
    assert len(UniqueNgrams("aaaa")) == 4
    assert len(UniqueNgrams("ababab")) == 11
    assert len(UniqueNgrams("tracking")) == 36  # For a string without repetitions,
                                                # the number of substrings should be
                                                # equal to the choose function.
    return

def test_StripString():
    assert StripString(r"a**@#~22uwuwuwu9u*$$m,..ii''") == "a22uwuwuwu9umii"
    assert StripString("") == ""
    assert StripString(")))))))))))))))))))£$%^^&*") == ""
    assert StripString(r""""'''''''''''""") == ""
    return


