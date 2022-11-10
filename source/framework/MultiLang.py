from aug22.source.framework import utilities
from aug22.source.framework.Language import Language
from aug22.source.framework.GetUserInput import GetUserInput


class MultiLang:

    def __init__(self, LangNameList):

        self.LangNameList = LangNameList
        self.LangList = []
        self.LangCount = len(self.LangNameList)

        for LangName in self.LangNameList:
            self.LangList.append(Language("wordfreq", LangName))

        return


