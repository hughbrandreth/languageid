

def GetUserInput():

    Languages = []
    textSources = []
    selectLanguages = False

    print("Please enter the addresses of the files you wish to analyse, then press 1:")

    while True:
        userSourceInput = str(input())
        if userSourceInput == "1":
            break
        else:
            textSources.append(userSourceInput)


    print("Do you wish to select Languages for comparison? type y/n:")
    Inputstring = input()

    if Inputstring == "y" or Inputstring == "Y":
        selectLanguages = True
        print("Enter Languages for comparison, then press 1")

        while True:
            userLangInput = str(input())
            if userLangInput == "1":
                break
            else:
                Languages.append(userLangInput)

    result = [textSources, selectLanguages, Languages]
    return result