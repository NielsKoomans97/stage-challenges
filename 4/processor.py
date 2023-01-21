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
                
    print(f"Vampires: {vampiresTotal}")
    print(f"Zombies : {zombiesTotal}")
    print(f"Witches : {witchesTotal}")
    print(f"Houses  : {housesTotal}")
            