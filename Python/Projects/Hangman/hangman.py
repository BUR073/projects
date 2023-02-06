"""Hangman
Standard game of Hangman. A word is chosen at random from a list and the
user must guess the word letter by letter before running out of attempts."""

import random

def main():
    welcome = ['Welcome to Hangman! A word will be chosen at random and',
               'you must try to guess the word correctly letter by letter',
               'before you run out of attempts. Good luck!'
               ]

    for line in welcome:
        print(line, sep='\n')

    # setting up the play_again loop

    play_again = True

    while play_again:
        # set up the game loop

        words = ['because', 'pelican', 'orangutan'] # Your bank of words for the hangman

        chosen_word = random.choice(words).lower()

        player_guess = None # will hold the players guess

        guessed_letters = [] # a list of letters guessed so far

        word_guessed = []
        
        for letter in chosen_word:
            word_guessed.append("-") # create an unguessed, blank version of the word
        joined_word = None # joins the words in the list word_guessed

        
#Extension - Visual 
        HANGMAN = (
"""
-----
|   |
|  
|
|
|
|
|
|
--------
""",
"""
Image -  1 error
""",
"""
Image - 2 error
""",
"""
Image - 3 Error
""",
"""
Image - 4 Error
""",
"""
Image - 5 Error
""",
"""
Image - 6 Error
""",
"""
Image - 7 Error
""",
"""
Image - 8 Error
""",
"""
Image - 9 Error
""",
"""
Image - 10 Error
""")

#First Section
        
        #Initialise the game - Reset your variable here
        
        
        #While you have lives or when there are "-"s left in your guess
        
        #Display the blank slots and letters guessed
            
#Extension - Data Validations
            
            # check valid input
                              
            
                # check the input is a letter. Also checks an input has been made.
                    
                # check the input is only one letter
                    
                # check it letter hasn't been guessed already
                   
###Main Section
            # Each letter that is guessed should be stored somewhere, add a line here to do that using the .append tool.

            #Check the work if it's in the chosen word
                 # replace all letters in the chosen word that match the players guess

            #Check if the guess is in the world if not take a attempt off
               
                

    # if no blanks remaining then win game
    #else check if there is any attempts left, if not end game message        
    # loop must have ended because attempts reached 0
            
            
###Loop back to top
        #ask the player if they want to play again and reset the game

if __name__ == "__main__":
    main()
