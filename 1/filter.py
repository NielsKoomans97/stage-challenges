import re
import os

print("Processing...")

with open('C:\\Users\\Niels.niels-pc\\Source\\Repos\\stage-challenges\\1\\input.txt', "r+") as inputFile:
    txt = inputFile.read()
    output = ""

    for line in txt.split('\n'):
        if line == "":
            output += "\n"
        else:
            line = re.sub("([\W]+)", " ", line)
            line = re.sub("([\d]+)", " ", line)
            line = line.replace("_"," ")

            words = re.findall("([A-Za-z0-9]+)",line)

            for i in range(0,len(words)):
                word = words[i]

                if i == len(words) - 1:
                    output += word + "\n"
                else:
                    output += word + " "

    with open('C:\\Users\\Niels.niels-pc\\Source\\Repos\\stage-challenges\\1\\output.txt',"w+") as outputFile:
        outputFile.write(output)
        outputFile.close()

    inputFile.close()

print("Processed")
