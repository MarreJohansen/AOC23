def main():
    array = []
    y = 0
    input = open("3.py/input1.txt").read().split("\n")
    for line in input:
            array.append(list(line))
    checkDirections(array)
        
def checkDirections(array): #array[rows][columns]
    check = False
    totalSum = 0
    max_y = len(array)-2 #max row
    number = ""
    for i1, row in enumerate(array): #i1 is y (row)
        max_x = len(row)-1 #max column
        for i2, currentVal in enumerate(row): #i2 is x (column)
            if (currentVal.isdigit()):
                if (check == True):
                    number += currentVal
                else:
                    number += currentVal
                    if (0 < i1): #check above
                        if not (array[i1-1][i2] == "." or array[i1-1][i2].isdigit()):
                            check = True
                    if (i1 < max_y): #check below
                        if not (array[i1+1][i2] == "." or array[i1+1][i2].isdigit()):
                            check = True
                    if (i2 < max_x): #check right
                        if not (array[i1][i2+1] == "." or array[i1][i2+1].isdigit()):
                            check = True
                    if (0 < i2): #check left
                        if not (array[i1][i2-1] == "." or array[i1][i2-1].isdigit()):
                            check = True
                    if (i2 < max_x and 0 < i1): #check nordost
                        if not (array[i1-1][i2+1] == "." or array[i1-1][i2+1].isdigit()):
                            check = True
                    if (i1 < max_y and i2 < max_x): #check sydost
                        if not (array[i1+1][i2+1] == "." or array[i1+1][i2+1].isdigit()):
                            check = True
                    if (0 < i1 and 0 < i2): #check nordvast
                        if not (array[i1-1][i2-1] == "." or array[i1-1][i2-1].isdigit()):
                            check = True
                    if (i1 < max_y and 0 < i2): #check sydvast
                        if not (array[i1+1][i2-1] == "." or array[i1+1][i2-1].isdigit()):
                            check = True
            else:
                if (check == True):
                    if number != "":
                        check = False
                        totalSum +=int(number)
                number = ""
    print(totalSum)

main()