## Hangman

import random 

def checkWhere(word, guess, attempts):

    x = 0 

    letter = word[x]

    if letter == guess:
        print("You guess is letter", x + 1, 'in the word')
        x = x + 1

    else:
        print("That letter is no in the word")
        
        x = x + 1

        visual(attempts)

        attempts = attempts + 1 
        return attempts 


def newWord():
    words = ['test']

    #words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
            #'coyote crow deer dog donkey duck eagle ferret fox frog goat '
            #'goose hawk lion lizard llama mole monkey moose mouse mule newt '
            #'otter owl panda parrot pigeon python rabbit ram rat raven '
            #'rhino salmon seal shark sheep skunk sloth snake spider '
            #'stork swan tiger toad trout turkey turtle weasel whale wolf '
            #'wombat zebra ').split()


    chosen_word = list(random.choice(words).lower())

    return(chosen_word)

def main():

    word = newWord()
    attempts = 6


    while attempts != 0:  
        guess = str(input("Input guess: "))
    

        if guess in word: 
            attempts = checkWhere(word, guess, attempts)
            attempts = attempts +  1
        

        else: 
            print("That letter is not in the word")
            attempts = attempts +  1

def visual(number):

    HANGMANPICS = ['''
    +---+
    |   |
        |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    /|   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    /|\ |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    /|\ |
    /   |
        |
    =========''', '''
    +---+
    |   |
    O   |
    /|\ |
    / \ |
        |
    =========''']

    print(HANGMANPICS[number])

    
    

if __name__ == "__main__":
    main()





     
