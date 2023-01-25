import re

with open('C:\\Users\\Niels.niels-pc\\source\\repos\\stage-challenges\\4\\input.txt', "r+") as inputFile:
    content = inputFile.read();

    vampiresTotal = 0
    zombiesTotal = 0
    witchesTotal = 0
    housesTotal = 0

    rulevampire = 3
    rulezombie = 4
    rulewitch = 5

    # Tekstlijnen parseren en onderverdelen in verschillende items
    for line in content.split("\n"):
        parts = line.split(",")
        for i in range(0,len(parts)):
            part = parts[i]
            print(f"    {part}")

            keyvaluepair = part.split(": ")

            if keyvaluepair[0].__contains__("Vampires"):
                vampiresTotal += int(keyvaluepair[1])
            if keyvaluepair[0].__contains__("Zombies"):
                zombiesTotal += int(keyvaluepair[1])
            if keyvaluepair[0].__contains__("Witches"):
                witchesTotal += int(keyvaluepair[1])
            if keyvaluepair[0].__contains__("Houses"):
                housesTotal += int(keyvaluepair[1])

    # Geparseerde tellingen nalopen
    vampireCandies = 0
    zombieCandies = 0
    witchCandies = 0

    for v in range(0,vampiresTotal):
        for i in range(0,housesTotal):
            vampireCandies += rulevampire

    for z in range(0, zombiesTotal):
        for i in range(0,housesTotal):
            zombieCandies += rulezombie

    for w in range(0, witchesTotal):
        for i in range(0,housesTotal):
            witchCandies += rulewitch

    # Eindresultaat uitprinten in de Console
    print(f"Vampires: {vampireCandies / housesTotal} candies per house (or {vampireCandies} candies total)")
    print(f"Zombies : {zombieCandies / housesTotal} candies per house (or {zombieCandies} candies total)")
    print(f"Witches : {witchCandies / housesTotal} candies per house (or {witchCandies} candies total)")
    print(f"Houses  : {housesTotal}")
