alphToNumb = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def main():
    total = 0
    with open("puzzle 1/input.txt") as f:
        for line in f:
            print(line)
            for key in alphToNumb:
                print(key)
                if (key in line):
                    print("ok")
                    line = line.replace(key, alphToNumb.get(key))
            total += int(loopy(line) + loopy(reversed(line)))
            print(total)
    return total

def loopy(line):
    for i in line:
        print(line)
        print(i)
        if(i.isdigit()):
            return i
        
def changeVal():
    

print(main())