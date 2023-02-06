def testDrive( actual, expected ):
    if actual == expected:
        print( "test succeeded", actual, " == ", expected )
    else:
        print( "test failed:", actual, " != ", expected )

wages = [ (17, 11, 3), (21, 1, 0), 19.25, 30.16, 23.37, 14.005 ]

notesAndCoins = [ (2000,"£20 note"), (1000,"£10 note"),
                  (500,"£5 note"), (100,"£1 note"),
                  (50,"50p"), (10,"10p"), (5,"5p"),
                  (2,"2p"), (1,"1p"), (0.5, "1/2p")]

requirements = {}
for (value,name) in notesAndCoins:
    requirements[name] = 0
    
checkWageTotal = 0
checkNotesCoinsValue = 0

for wage in wages:
    wage = wage * 100
    checkWageTotal = checkWageTotal + wage
    for (value,name) in notesAndCoins:
        required = 0
        while wage >= value:
            wage = wage - value
            checkNotesCoinsValue = checkNotesCoinsValue + value
            required += 1
        requirements[name] += required
    # check that value of wage is zero

for item in requirements.keys():
    print("{:10s} {:5d}".format(item,requirements[item]))

if checkWageTotal == checkNotesCoinsValue:
    print("Cross tabulation correct")

