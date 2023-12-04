alphToNumb = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def main():
    total = 0
    with open("puzzle 1/input.txt") as f:
        for line in f:
            listOfStartIndexes = {}
            #print(line)
            for key in alphToNumb:
                #print(key)
                if (key in line):
                    #print("ok")
                    listOfStartIndexes[line.find(key)] = key
                    #line = line.replace(key, alphToNumb.get(key))
            sortedIndexes = dict(sorted(listOfStartIndexes.items()))
            print(sortedIndexes)
            for index in sortedIndexes:
                word = sortedIndexes.get(index)
                line = line.replace(word, alphToNumb.get(word))
            print(line)
            total += int(loopy(line) + loopy(reversed(line)))
            #print(total)
    return total

def loopy(line):
    print(line)
    for i in line:
        if(i.isdigit()):
            return i
        
#def changeVal():
    

print(main())