from datetime import datetime
from tkinter.ttk import Combobox
from tkinter.filedialog import *
import PIL.Image
import PIL.ImageTk
from statistics import mean

from aug22.source.Timelogger import TimeLogsDict
from aug22.source.framework.GrandAnalysis import GrandAnalysis
from aug22.source.framework.utilities import FullLangList
from aug22.source.LanguageManager import LanguageManager
from aug22.source.framework.Comparison import Comparison
from aug22.source.framework.Language import Language
from aug22.source.framework.GetUserInput import GetUserInput
from aug22.source.framework.Text import Text
from tkinter import *

import os


OutputDir = "E:\Hugh\HDD Documents\Birkbeck\Project\Outputs"
InputDir = r"E:/Hugh/HDD Documents/Python Programs/Decipheronator/source/sampleTexts"

FullTextList = []
FullAlgorithmList = ["HammingMatch", "LetterFreqComp", "PerfectMatch", "PerfectMatchOnFirst5Words", "PerfectMatchOnFirst10Words", "PerfectMatchOnFirst20Words", "LevenshteinMatch", "SubStringMatch"]
DefaultAlgorithm = "GetPerfectMatchScore"
ConfigModeBool = False


for file in os.listdir(InputDir):
    if file.endswith(".txt"):
        FullTextList.append(file)

def OpenExcelFile():
    os.startfile(ExcelFileName)
    return

def OpenCsvFile():
    os.startfile(CsvFileName)
    return

def OpenTextFile():
    os.startfile(TextFileName)
    return


def GenerateExcel():
    '''Initiates construction of an excel spreadsheet labelled with the time the analysis was performed at, and allows the user to open it.'''
    global ExcelFileName
    ExcelFileName = OutputDir + r"\testexcelfile" + str(FinishTime) + ".xlsx"
    BigTest.SaveAsExcel(ExcelFileName)
    ExcelGenButton.place_forget()
    OpenExcelButton = Button(window, text="Open", bg="white", fg="black", font=("calibri", 10, "bold"), command=OpenExcelFile)
    OpenExcelButton.place(x=50, y=450)
    return

def GenerateCsv():
    '''Initiates construction of a csv file labelled with the time the analysis was performed at, and allows the user to open it.'''
    global CsvFileName
    CsvFileName = OutputDir + r"\testcsvfile" + str(FinishTime) + ".csv"
    BigTest.SaveAsCsv(CsvFileName)
    CsvGenButton.place_forget()
    OpenCsvButton = Button(window, text="Open", bg="white", fg="black", font=("calibri", 10, "bold"), command=OpenCsvFile)
    OpenCsvButton.place(x=150, y=450)

def GenerateText():
    '''Initiates construction of a text file labelled with the time the analysis was performed at, and allows the user to open it.'''
    global TextFileName
    TextFileName = OutputDir + r"\testtextfile" + str(FinishTime) + ".txt"
    BigTest.SaveAsText(TextFileName)
    TextGenButton.place_forget()
    OpenTextButton = Button(window, text="Open", bg="white", fg="black", font=("calibri", 10, "bold"), command=OpenTextFile)
    OpenTextButton.place(x=250, y=450)

def DisplayOutput():
    '''
    Shows the result of the analysis to the user.
    If the user has made only one request, the answer is displayed directly.
    If the user has made multiple requests, then the answers are not displayed but can be viewed in exported files.
    No parameters: the results information is extracted by the function.

    :return: None
    '''
    ResultsTitleLabel = Label(window, text="Results", bg="white", fg="black", font=("Calibri", 14, "bold"))
    ResultsTitleLabel.place(x=50, y=50)

    if len(BigTest.AlgorithmNameList) == 1 and len(BigTest.TextList) == 1:
        ResultLabel = Label(window, text="This text is most likely written in " + BigTest.BestScoringLangArray[0, 0], bg="white", fg="black", font=("Calibri", 10, "bold"))
        ResultLabel.place(x=50, y=100)
    else:
        ResultLabel = Label(window, text="There are several results. To view them, see below.", bg="white", fg="black", font=("Calibri", 10, "bold"))
        ResultLabel.place(x=50, y=100)



def ShowOutputOptions():

    '''
    Shows the user options for how to export the results of the analysis.
    The user can select file formats, which initiates the construction of a file which the user can then open.
    Takes no parameters.

    :return: None
    '''

    # Label
    OutputLabel = Label(window, text="Outputs", bg="white", fg="black", font=("Calibri", 14, "bold"))
    OutputLabel.place(x=50, y=375)
    OutputDescLabel = Label(window, text="If you wish to see the full results, select a format to present them:", bg="white", fg="black", font=("Calibri", 10))
    OutputDescLabel.place(x=50, y=400)


    # Output Format Requests

    # Excel Spreadsheet
    # Icon
    global ExcelImg
    ExcelImg = PIL.ImageTk.PhotoImage(PIL.Image.open(r"E:\Hugh\HDD Documents\Python Programs\Decipheronator\source\images\ExcelLogo.jpg"))
    # Text
    ExcelLabel = Label(window, text="Excel", bg="white", fg="black", font=("Calibri", 8))
    ExcelLabel.place(x= 50, y=425)
    # Button to Trigger Creation
    global ExcelGenButton
    ExcelGenButton = Button(window, image=ExcelImg, bg="white", fg="black", font=("Calibri", 8), command=GenerateExcel)
    ExcelGenButton.place(x=50, y=450)

    # Csv File
    # Icon
    global CsvImg
    CsvImg = PIL.ImageTk.PhotoImage(PIL.Image.open(r"E:\Hugh\HDD Documents\Python Programs\Decipheronator\source\images\CsvLogo.jpg"))
    # Text
    CsvLabel = Label(window, text="Csv", bg="white", fg="black", font=("Calibri", 8))
    CsvLabel.place(x=150, y=425)
    # Button to Trigger Creation
    global CsvGenButton
    CsvGenButton = Button(window, image=CsvImg, bg="white", fg="black", font=("Calibri", 8), command=GenerateCsv)
    CsvGenButton.place(x=150, y=450)

    # Text File
    # Icon
    global TextImg
    TextImg = PIL.ImageTk.PhotoImage(PIL.Image.open(r"E:\Hugh\HDD Documents\Python Programs\Decipheronator\source\images\TextLogo.jpg"))
    # Text
    TextLabel = Label(window, text="Text", bg="white", fg="black", font=("Calibri", 8))
    TextLabel.place(x= 250, y=425)
    # Button to Trigger Creation
    global TextGenButton
    TextGenButton = Button(window, image=TextImg, bg="white", fg="black", font=("Calibri", 8), command=GenerateText)
    TextGenButton.place(x=250, y=450)

    # Directory
    OutputDirLabel = Label(window, text="Files saved in:\n" + OutputDir, justify=LEFT, bg="white", fg="black", font=("Calibri", 8))
    OutputDirLabel.place(x=50, y=500)


    # Exit Button
    ExitButton = Button(window, text="Exit", bg="white", fg="black", font=("calibri", 18, "bold"), command=exit)
    ExitButton.place(x=1050, y=500)


    return


def Execute():
    '''
    This function runs the core of the system:
    The config menus and run button are closed, then the object which handles the analysis is constructed.
    The analysis function of the object is then initiated.
    The results are then provided to the user.
    No parameters are given to the function - data is extracted by the function.

    :return: None
    '''

    # Closing the run button
    RunButton.place_forget()

    # Closing the configuration menus
    TextLabel.place_forget()
    TextDescr.place_forget()
    TextListBox.place_forget()
    SelectAllTextButton.place_forget()
    InputDirLabel.place_forget()

    Langlabel.place_forget()
    LangDescr.place_forget()
    LangListbox.place_forget()
    SelectAllLangBox.place_forget()

    AlgorithmLabel.place_forget()
    AlgorithmDescr.place_forget()
    AlgorithmListbox.place_forget()
    SelectAllAlgorithmbox.place_forget()

    # Recording the selections made by the user
    TextList = [TextListBox.get(i) for i in TextListBox.curselection()]
    LangList = [LangListbox.get(i) for i in LangListbox.curselection()]

    if AlgorithmListbox.curselection() == None:
        AlgorithmList = [DefaultAlgorithm]
    else:
        AlgorithmList = [AlgorithmListbox.get(i) for i in AlgorithmListbox.curselection()]

    # creating an analysis object tailored to the user's requests
    global BigTest
    BigTest = GrandAnalysis(TextList, LangList, AlgorithmList)
    global FinishTime

    # Recording when the analysis takes place to label output files.
    FinishTime = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Showing the results to the user and providing the user with more options.
    DisplayOutput()
    ShowOutputOptions()

    return


window = Tk()
window.title("Language Analysis")
window.geometry("1200x625+10+10")
window.config(bg="white")
variables = []



###   Text   ###

# Title
TextLabel = Label(window, text="Text", bg="white", fg="black", font=("Calibri", 14, "bold"))
TextLabel.place(x=50, y=50)

# Description
TextDescr = Label(window, text="Which pieces of text would you like to examine?", justify=LEFT, bg="white",
                       fg="black", font=("Calibri", 10, "bold"))
TextDescr.place(x=50, y=100)

# Button
SelectAllTextintvar = IntVar()


def SelectAllTextbuttonclick():
    if bool(SelectAllTextintvar.get()):
        TextListBox.select_set(0, END)
    else:
        TextListBox.select_clear(0, END)
    return


SelectAllTextButton = Checkbutton(window, text="Select All Texts", bg="white", variable=SelectAllTextintvar,
                                  command=SelectAllTextbuttonclick)
SelectAllTextButton.place(x=50, y=140)

# ListBox
ChosenTextVar = StringVar(value=sorted(FullTextList))
TextListBox = Listbox(window, listvariable=ChosenTextVar, bg="white", selectmode="multiple", width=50)
TextListBox.place(x=50, y=180)
TextListBox.configure(exportselection=False)

# Directory Label
InputDirLabel = Label(window, text = "Files Retrieved from:\n" + InputDir, justify=LEFT, bg="white", fg="black", font=("Calibri", 10))
InputDirLabel.place(x=50, y=350)


###   Language   ###

# Title
Langlabel = Label(window, text="Language", bg="white", fg="black", font=("Calibri", 14, "bold"))
Langlabel.place(x=400, y=50)

# Description
LangDescr = Label(window, text="Select which languages you wish to compare your text to", justify=LEFT,  bg="white", fg="black", font=("Calibri", 10, "bold"))
LangDescr.place(x=400, y=100)

# Button
SelectAllLangintvar = IntVar()
def SelectAllLangbuttonclick():
    if bool(SelectAllLangintvar.get()):
        LangListbox.select_set(0, END)
    else:
        LangListbox.select_clear(0, END)
    return

SelectAllLangBox = Checkbutton(window, text="Select All Languages", bg="white", variable=SelectAllLangintvar, command=SelectAllLangbuttonclick)
SelectAllLangBox.place(x=400, y=140)

# List Box
ChosenLangvar = StringVar(value=sorted(FullLangList))
LangListbox = Listbox(window, listvariable=ChosenLangvar, bg="white", selectmode="multiple", width=20, height=10)
LangListbox.place(x=400, y=180)
LangListbox.configure(exportselection=False)



###   ALGORITHMS   ###
# Algorithm Selection Interface

# Title
AlgorithmLabel = Label(window, text="Algorithm", bg="white", fg="black", font=("Calibri", 14, "bold"))
AlgorithmLabel.place(x=750, y=50)

# Description
AlgorithmDescr = Label(window,
                       text="Do you wish to choose which types of Analysis (Algorithms) to perform?\nOtherwise, the default algorithm, Levenshtein will be used.",
                       justify=LEFT, bg="white", fg="black", font=("Calibri", 10, "bold"))
AlgorithmDescr.place(x=750, y=100)

# Button
ChooseAlgorithmintvar = IntVar()
def SelectAllAlgorithmbuttonclick():
    if bool(ChooseAlgorithmintvar.get()):
        AlgorithmListbox.select_set(0, END)
    else:
        AlgorithmListbox.select_clear(0, END)


SelectAllAlgorithmbox = Checkbutton(window, text="Select All Algorithms", bg="white", variable=ChooseAlgorithmintvar,
                                    command=SelectAllAlgorithmbuttonclick)
SelectAllAlgorithmbox.place(x=750, y=140)

# List Box
ChosenAlgorithmvar = StringVar(value=sorted(FullAlgorithmList))
AlgorithmListbox = Listbox(window, listvariable=ChosenAlgorithmvar, bg="white", selectmode="multiple", width=50)
AlgorithmListbox.place(x=750, y=180)
AlgorithmListbox.configure(exportselection=False)



# EXECUTION
# Button to Execute the system process
RunButton = Button(window, text="Run", bg="white", fg="black", font=("Calibri", 28, "bold"), command=Execute)
RunButton.place(x=1050, y=500)



window.mainloop()





