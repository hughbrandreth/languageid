from aug22.source.framework.GrandAnalysis import *



def test_GrandAnalysis():
    TextList = ["longtext.txt"]
    LangList = ["en", "nl", "fr"]
    TestGrandAnalysis = GrandAnalysis(TextList, LangList, ["PerfectMatch", "PerfectMatchOnFirst5Words", "PerfectMatchOnFirst10Words", "PerfectMatchOnFirst20Words"])
    TestGrandAnalysis.GenerateComparisons()
    assert TestGrandAnalysis.SuccessfullyInitialised
    assert TestGrandAnalysis.GetBestScoringLang("PerfectMatchOnFirst5Words", 0) == "en"
    assert TestGrandAnalysis.AlgorithmCount == 4
    assert numpy.shape(TestGrandAnalysis.ScoreArray) == (3, 4, 1)

    EmptyTextList = []
    LangList = ["en", "nl", "fr"]
    NoTextFileTestGrandAnalysis = GrandAnalysis(EmptyTextList, LangList, ["PerfectMatch", "PerfectMatchOnFirst5Words", "PerfectMatchOnFirst10Words", "PerfectMatchOnFirst20Words"])
    assert not NoTextFileTestGrandAnalysis.SuccessfullyInitialised
    NoTextFileTestGrandAnalysis.GenerateComparisons()
    assert NoTextFileTestGrandAnalysis.GetBestScoringLang(0, 0) == "??"

    return


