letA = ["   AAA   ",
        "AAA   AAA",
        "AA     AA",
        "AAAAAAAAA",
        "AA     AA",
        "AA     AA",
        "AA     AA"]

letB = ["BBBBBBBBB",
        "BB     BB",
        "BB     BB",
        "BBBBBBBBB",
        "BB     BB",
        "BB     BB",
        "BBBBBBBBB"]

letC = [" CCCCCCCC",
        "CC       ",
        "CC       ",
        "CC       ",
        "CC       ",
        "CC       ",
        " CCCCCCCC"]

letD = ["DDDDDDDD ",
        "DD     DD",
        "DD     DD",
        "DD     DD",
        "DD     DD",
        "DD     DD",
        "DDDDDDDDD"]

letE = ["EEEEEEEEE",
        "EE       ",
        "EE       ",
        "EEEEEEEEE",
        "EE       ",
        "EE       ",
        "EEEEEEEEE"]


letI = ["IIIIIIIII",
        "   II    ",
        "   II    ",
        "   II    ",
        "   II    ",
        "   II    ",
        "   II    ",
        "IIIIIIIII"]




def letterA():
    for line in letA:
        print(line) 

    print("")

def letterB():
    for line in letB:
        print(line)
        
    print("")

def letterC():
    for line in letC:
        print(line)
        
    print("")

def letterD():
    for line in letD:
        print(line)
        
    print("")

def letterE():
    for line in letE:
        print(line)
        
    print("")

def letterI():
    for line in letI:
        print(line)

    print("")


x = int(input("How many letters would you like to print"))

list = [""]

while x > 0:
    
    letter_one = str(input(":"))
    lettera = ("letter" + letter_one + "()")

    x -= 1

    if lettera == "letterA()":
        letterA()

    elif lettera == "letterB()":
        letterB()

    elif lettera == "letterC()":
        letterC()

    elif lettera == "letterD()":
        letterD()

    elif lettera == "letterE()":
        letterE()

    elif lettera == "letterI()":
        letterI()








