def main():
    winningNumbers = []
    checkNumbers = []
    copiesDict = []
    totalCardPoints = 0
    input = open("puzzle 4/input.txt").read().split("\n")
    for line in input:
        templateList = line.split(" ")[2:]
        separatorIndex = templateList.index('|')
        winningNumbers = templateList[:separatorIndex]
        winningNumbers = [item for item in winningNumbers if item != '']
        checkNumbers = templateList[separatorIndex + 1:]
        checkNumbers = [item for item in checkNumbers if item != '']
        totalCardPoints += checkFunc(winningNumbers, checkNumbers)[0]
        copiesDict.append([1, winningNumbers, checkNumbers])
    totalScratchCards = copiesFunc(copiesDict)
    return totalCardPoints, totalScratchCards

def copiesFunc(copiesDict):
    totalScratchcards = 0
    nrOfCards = len(copiesDict) - 1
    for index, num in enumerate(copiesDict):
        countVal = checkFunc(num[1], num[2])[1]
        if (countVal != 0):
            for i in range(1, countVal+1):
                if not (index+i > nrOfCards):
                    copiesDict[index+i][0] += num[0]
    for scratchCard in copiesDict:
        totalScratchcards += scratchCard[0]
    return totalScratchcards

def checkFunc(winNumbers, checkNumbers):
    first_val = False
    count = 0
    scratchCount = 0
    for win in winNumbers:
        for check in checkNumbers:
            if (check == win):
                if (first_val == True):
                    count *= 2
                else:
                    first_val = True
                    count += 1
                scratchCount += 1
    return count, scratchCount

print(main())