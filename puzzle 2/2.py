def main():
    totalCount = 0
    lowestTotalCount = 0
    gameDict = {}
    with open("/Users/marre/Desktop/AOC2023/2/input.txt") as f:
        for line in f:
            (key, val) = line.split(": ")
            games = val.split(";")
            if (checkValid(games)):
                totalCount += int(key.split(" ")[1])
            lowestTotalCount += checkLowest(games)
    return ("Totalcount: " + str(totalCount) + " LowestTotalCount: " + str(lowestTotalCount)) 

def checkValid(games):
    for game in games:
        red = 0
        green = 0
        blue = 0
        cubes = game.split(", ")

        for cube in cubes:
            cube = cube.lstrip()
            cubeVal = cube.split(" ")[0]
            color = cube.split(" ")[1]
            color = color.rstrip()
            match color:
                case "red":
                    red += int(cubeVal)
                case "blue":
                    blue += int(cubeVal)
                case "green":
                    green += int(cubeVal)

        if not (red <= 12 and green <= 13 and blue <= 14):
            return False
    return True

def checkLowest(games):
    red = 0
    blue = 0
    green = 0

    for game in games:
        cubes = game.split(", ")

        for cube in cubes:
            cube = cube.lstrip()
            cubeVal = cube.split(" ")[0]
            color = cube.split(" ")[1]
            color = color.rstrip()
            match color:
                case "red":
                    if int(cubeVal) >= red:
                        red = int(cubeVal)
                case "blue":
                    if int(cubeVal) >= blue:
                        blue = int(cubeVal)
                case "green":
                    if int(cubeVal) >= green:
                        green = int(cubeVal)
    return red*green*blue

print(main())

