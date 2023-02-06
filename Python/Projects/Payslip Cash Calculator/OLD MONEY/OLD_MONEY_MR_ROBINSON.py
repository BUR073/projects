def testDrive( actual, expected ):
    if actual == expected:
        print( "test succeeded", actual, " == ", expected )
    else:
        print( "test failed:", actual, " != ", expected )

def addLSD( lhs, rhs ):

    resultL = 0
    resultS = 0
    resultD = 0
    
    resultD = lhs[2] + rhs[2]
    if resultD >= 12:
        resultD -= 12
        resultS += 1
    resultS += lhs[1] + rhs[1]
    if resultS >= 20:
        resultS -= 20
        resultL += 1    
    resultL += lhs[0] + rhs[0]
    return (resultL, resultS, resultD )

def subtractLSD( lhs, rhs ):

    resultL = lhs[0]-rhs[0]
    resultS = lhs[1]-rhs[1]
    resultD = lhs[2]-rhs[2]
    
    if resultD < 0:
        resultD += 12
        resultS -= 1

    if resultS < 0:
        resultS += 20
        resultL -= 1    

    return (resultL, resultS, resultD )

def quantityValue( value, quantity ):
    result = (0,0,0)
    for i in range(quantity):
        result = addLSD( result, value )
    return result

def greaterThanEqualLSD( lhs, rhs ):
    return lhs[0] >= rhs[0] and lhs[1] >= rhs[1] and lhs[2] >= rhs[2]

testDrive( addLSD( (17,11,3), (21,10,3) ), (39,1,6) )
testDrive( subtractLSD( (21,10,3), (17,11,3)), (3,19,0) )
testDrive( quantityValue( (0,2,6), 8 ), (1,0,0) )
testDrive( greaterThanEqualLSD( (1,1,2), (1,1,1) ), True )
testDrive( greaterThanEqualLSD( (2,1,2), (3,1,1) ), False )
           
wages = [ (17,11,3), (21,0,10), (19,5,0), (30,3,3), (23,7,6), (14, 0, 0.5) ]

notesAndCoins = [ ((20,0,0),"£20 note"), ((10,0,0),"£10 note"),
                  ((5,0,0),"£5 note"), ((1,0,0),"£1 note"),
                  ((0,10,0),"10s note"), ((0,2,6),"half crown"),
                  ((0,2,0),"2s"), ((0,1,0),"1s"),
                  ((0,0,6),"6d"), ((0,0,3),"3d"),
                  ((0,0,1),"1d"), ((0,0,0.5),"1/2d")]

requirements = {}
for (value,name) in notesAndCoins:
    requirements[name] = 0
    
checkWageTotal = (0,0,0)
checkNotesCoinsValue = (0,0,0)

for wage in wages:
    checkWageTotal = addLSD(checkWageTotal,wage)
    for (value,name) in notesAndCoins:
        required = 0
        while greaterThanEqualLSD(wage,value):
            wage = subtractLSD(wage,value)
            checkNotesCoinsValue = addLSD(checkNotesCoinsValue,value)
            required += 1
        requirements[name] += required

for item in requirements.keys():
    print("{:10s} {:5d}".format(item,requirements[item]))

if greaterThanEqualLSD(checkWageTotal,checkNotesCoinsValue) and greaterThanEqualLSD(checkNotesCoinsValue,checkWageTotal):
    print("Cross tabulation correct")
               
