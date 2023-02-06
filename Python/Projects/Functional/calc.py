def checkIfPrime(number): 
    if number <= 1:
        return("Not greater than 1")

    itself = number%number
    loopNumber = number
    while loopNumber != 2: 
        modNumber = number % loopNumber 
        loopNumber = loopNumber - 1
        if modNumber == 0:
            return(number,"is a prime - first")


    return(number, "is not a prime")






print(checkIfPrime(1))
print(checkIfPrime(5))
print(checkIfPrime(7))
print(checkIfPrime(48))