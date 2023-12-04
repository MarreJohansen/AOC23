alphToNumb = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def main():
    total = 0
    with open("puzzle 1/input.txt") as f:
        for line in f:
            listOfStartIndexes = {}
            for key in alphToNumb:
                if (key in line):
                    listOfStartIndexes[line.find(key)] = key
            sortedIndexes = dict(sorted(listOfStartIndexes.items()))
            for index in sortedIndexes:
                word = sortedIndexes.get(index)
                line = line.replace(word, alphToNumb.get(word))
            total += int(loopy(line) + loopy(reversed(line)))
    return total

def loopy(line):
    for i in line:
        if(i.isdigit()):
            return i   

print(main())