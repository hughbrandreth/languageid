from aug22.source.framework.Text import Text


class MultiText:

    def __init__(self, fileNameList):


        self.TextList = []
        self.comments = []

        for fileName in fileNameList:

            file = open(fileName, "r", encoding = "utf8")
            for Line in file.readlines():
                if Line[0] == "#":
                    self.comments.append(Line.strip())
                else:
                    self.TextList.append(Text(Line.strip()))

        self.TextCount = len(self.TextList)

        return