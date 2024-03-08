def theGoodShipInput(input: str) -> str:
    inputList = input.splitlines()
    nameSetsCount = int(inputList[0])
    start = 1
    output = ""
    for i in range(nameSetsCount):
        X, Y = inputList[start].split(" ")
        X = int(X)
        Y = int(Y)
        XList = inputList[start+1:start+X+1]
        YList = inputList[start+X+1:start+X+1+Y]
        outputNamesList = []
        for name in XList:
            if name not in YList:
                outputNamesList.append(name)
        outputNamesList.sort()
        output += "\n".join(outputNamesList)
        output += "\n\n"
        start = start+X+1+Y
    return output.strip()

#print(theGoodShipInput("3\n8 2\nCannon\nEngine\nHelm\nDeck\nAnchor\nCompass\nRadar\nLog\nDeck\nEngine\n6 3\nSteering\nGenerator\nWinches\nSuperstructure\nHull\nStern\nStern\nGenerator\nSteering\n4 3\nCargo\nBow\nAnchor\nEngine\nEngine\nBow\nAnchor"))