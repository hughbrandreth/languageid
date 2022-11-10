import csv


class Output:

    def __init__(self, GrandAnalysis):

        self.GrandAnalysis = GrandAnalysis

        return






def csvtable(table, fileName):
    file = open(fileName, "w", newline="")
    writer = csv.writer(file)
    for Row in table:
        writer.writeRow(Row)
    return







