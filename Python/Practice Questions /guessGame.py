NumberToGuess = input('Player One enter your chosen number: ')

while int(NumberToGuess) < 1 or int(NumberToGuess) > 10:
    NumberToGuess = input('Not a valid choice, please enter another number: ')

  

Guess = 0
NumberofGuesses = 0 

while Guess != NumberToGuess and NumberofGuesses < 5: 
    Guess = int(input("Player Two have a guess: "))
    NumberofGuesses = NumberofGuesses + 1 
    break


if int(Guess) == int(NumberToGuess):
    print("Player Two wins")

elif NumberofGuesses > 5: 
    print("Player One wins")






