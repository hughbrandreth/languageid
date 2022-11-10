import os

from aug22.source.framework.Language import Language


class LanguageManager:

    def __init__(self):

        self.LanguageDict = {}
        for fileName in os.listdir("E:\Hugh\HDD Documents\Python Programs\Decipheronator\source\languagetexts"):
            LanguageName = fileName[:-4]
            self.LanguageDict[LanguageName] = Language("E:/Hugh/HDD Documents/Python Programs/Decipheronator/source/languagetexts/" + fileName)

    def GetLanguage(self, LanguageName):
        return self.LanguageDict[LanguageName]

    def GetDict(self):
        return self.LanguageDict

