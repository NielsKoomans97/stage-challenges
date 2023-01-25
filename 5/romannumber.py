nr = input("Nummer > ")
resultnr = ""

if len(nr) >= 1000:
    for number in range(0,int(nr[0])):
        resultnr += "M"

    for number in range(0,int(nr[1])):
