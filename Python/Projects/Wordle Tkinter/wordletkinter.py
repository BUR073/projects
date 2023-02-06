import random
from tkinter import *

## Frontend

def setup():

    window = Tk()
    # add widgets here

    window.title('Wordle')
    window.geometry("500x500+10+20")
    window.mainloop()

    canvas = Canvas(master, width=500, height=500)
    canvas.create_rectangle(100, 100, 100, 100, fill="blue", outline = 'blue')


## Backend

def ChooseWord(): 
#out of 1 - 5757
  LineNum = random.randint(1,5757)

  f=open('words.txt')
  lines = f.readlines()

  wordle = lines[LineNum]
  print(wordle)
  return(wordle)


wordle = ChooseWord()


attempt = 0

def write() : 
  
  global attempt 
 

  while attempt != 6:
    print('')
    print('')
    print("Attempt: ", attempt + 1)
    guess = str(input("Input guess: "))
    number = containsNumber(guess)

    if len(guess) < 5 or len(guess) > 5: 
      print("Please enter 5 letters ")
      write()
    

    elif number == True:
      print("Please enter 5 letters without a number")
      write() 


    values = CheckGuess(guess)
    
    attempt = attempt + 1

    if values == [2, 2, 2, 2, 2]:
      print('')
      print("Success in", (attempt), "attempts")
      
      return

    elif attempt == 5:
      print('')
      print("You have used all you attempts")
      print("The wordle was:", wordle)
      return
   
  # 0 = Black, 1 = Yellow, 2 = Green


  


def containsNumber(value):
    for character in value:
        if character.isdigit():
            return True
    return False

def CheckGuess(guess):
  values = []
  check = 0
  guess_array = list(guess)
  wordle_array = list(wordle)
  
  while check != 6:
    cmpGuess = guess_array[check]
    cmpWordle = wordle_array[check]
  

    if cmpGuess == cmpWordle:
      print("Letter", check, "is Green")
      values.append(2)

    elif cmpGuess in wordle_array:
      print("Letter", check, "is Yellow")
      values.append(1)


    else:
      print("Letter", check, "is Black")
      values.append(0)

    check = check + 1

  return(values)

setup()
write()