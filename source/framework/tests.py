from datetime import *
from matplotlib import pyplot
import cProfile
import numpy
from aug22.source.Timelogger import TimeLogsDict
from aug22.source.framework.GrandAnalysis import GrandAnalysis
from aug22.source.framework.Comparison import Comparison
from aug22.source.framework.Language import Language
from aug22.source.resultsprocessing.Table import Table
from aug22.source.framework.Text import Text

WordFreq_bigrams = [
'ar','bn','bg','ca','zh','cs','da','nl','en','fi','fr','de','el','he','hi','hu','is','id','it','ja','ko','lv','lt','mk','ms','nb','fa','pl','pt','ro','ru','sh','sl','sk','es','sv','fil','ta','tr','uk','ur','vi'
]

######## Text Addresses to use in the running of the system:  ########

# E:/Hugh/HDD Documents/Python Programs/Decipheronator/source/sampletexts/chaucersamplelangcommentry.txt
# E:/Hugh/HDD Documents/Python Programs/Decipheronator/source/sampletexts/en_news_scraped_from_wikipedia_with_lang_tag.txt
# E:/Hugh/HDD Documents/Python Programs/Decipheronator/source/sampletexts/fr_sentences_from_wiki_with_lang_tag.txt

########                                                      ########

# def testfunc():
#
#     bigtest = GrandAnalysis()
#     bigtest.inputwindow()
#     #bigtest.saveasexcel(r"E:\Hugh\HDD Documents\Birkbeck\Project\Outputs\testexcelfile" + datetime.now().strftime("%Y%m%d_%H%M%S") +".xlsx")
#     return
#
# testfunc()

#cProfile.run("testfunc()")
#
# testArray = numpy.Array([[1, 0, 23, 4], [7, 8, 2, 16]])
# title = "fruitchart"
# rows = ["apples", "oranges"]
# columns = ["adrian", "brian", "colin", "daniel"]
# testtable = Table(rows, columns, testArray, title)
# print(testtable.aslist())
# csvname = r"E:\Hugh\HDD Documents\Birkbeck\Project\Outputs\testcsvfile.csv"
# xlsxname = r"E:\Hugh\HDD Documents\Birkbeck\Project\Outputs\testexcelfile.xlsx"
# testtable.outputtocsv(csvname)
# testtable.outputtoxlsx(xlsxname)


file = open("E:/Hugh/HDD Documents/Python Programs/Decipheronator/source/sampletexts/longtext.txt", "r", encoding="utf8")
Text = Text(file.readlines()[0].strip(), "test")


french = Language("wordfreq", "fr")
frenchComparison = Comparison(Text, french)
frenchComparison.CompareLetterFreqDistributions()
print("french: ", frenchComparison.FreqDiff)


english = Language("wordfreq", "en")
englishComparison = Comparison(Text, english)
englishComparison.CompareLetterFreqDistributions()
print("english: ", englishComparison.FreqDiff)


dutch = Language("wordfreq", "nl")
dutchComparison = Comparison(Text, dutch)
dutchComparison.CompareLetterFreqDistributions()
print("dutch: ", dutchComparison.FreqDiff)

russian = Language("wordfreq", "ru")
russianComparison = Comparison(Text, russian)
russianComparison.CompareLetterFreqDistributions()
print("russian: ", russianComparison.FreqDiff)
