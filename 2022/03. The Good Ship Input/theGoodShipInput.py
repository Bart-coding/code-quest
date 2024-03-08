def theGoodShipInput(input: str) -> str:
    inputList = input.splitlines()
    nameSetsCount = int(inputList[0])
    nameSetStartIndex = 1
    output = ""
    for i in range(nameSetsCount):
        X, Y = inputList[nameSetStartIndex].split(" ")
        X = int(X)
        Y = int(Y)
        XList = inputList[nameSetStartIndex + 1 : nameSetStartIndex + X+1]
        YList = inputList[nameSetStartIndex + X+1 : nameSetStartIndex + X+1+Y]
        outputNamesList = []
        for name in XList:
            if name not in YList:
                outputNamesList.append(name)
        outputNamesList.sort()
        output += "\n".join(outputNamesList)
        output += "\n\n"
        nameSetStartIndex = nameSetStartIndex + X+1+Y
    return output.strip()

#print(theGoodShipInput("3\n8 2\nCannon\nEngine\nHelm\nDeck\nAnchor\nCompass\nRadar\nLog\nDeck\nEngine\n6 3\nSteering\nGenerator\nWinches\nSuperstructure\nHull\nStern\nStern\nGenerator\nSteering\n4 3\nCargo\nBow\nAnchor\nEngine\nEngine\nBow\nAnchor"))