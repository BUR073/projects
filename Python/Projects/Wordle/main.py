import random
import turtle

tr = turtle.Turtle()

#turtle.write
turtle.tracer(0, 0)
tr.speed(0)
turtle.Screen().bgcolor("black")
turtle.hideturtle()

def newLine(currentLine):
  coords = [(-200, 150), (-200, 80), (-200, 10), (-200, -60), (-200, -130), (-200, -200), (-200, -270)]

  newLineCoords = coords[currentLine]
  
  tr.penup()
  tr.goto(newLineCoords)
  tr.pendown()

def drawBox(colour):
  tr.fillcolor(colour)
  tr.begin_fill()
  for i in range(2):
    tr.forward(50)
    tr.right(90)
    tr.forward(50)
    tr.right(90)
  tr.end_fill()
  tr.penup()
  tr.forward(75)
  tr.pendown() 
  turtle.update()

def setup(): 
  tr.penup()
  tr.goto(-80, 175)
  tr.pendown()
  tr.color("white")
  tr.write("Wordle", font=("Arial", 20, "bold"))

  tr.penup()
  tr.goto(-207, 155)
  tr.pendown()

  tr.fillcolor('dark grey')
  tr.begin_fill()

  for i in range(2):
    tr.forward(364)
    tr.right(90)
    tr.forward(340)
    tr.right(90)

  tr.end_fill()

  line = 0
  square = 0

  while square < 5: 
    newLine(square)
    drawBox('white')
    drawBox('white')
    drawBox('white')
    drawBox('white')
    drawBox('white')
    
    square = square + 1

  turtle.update() 

  turtle.update()
  tr.penup()
  tr.goto(-200, 150)
  tr.pendown()

setup()

def turtleLetters(guessArray, attempt):
  turtle.color('white')
  coords = [(-185, 105), (-185, 30), (-185, -35), (-185, -105), (-185, -180), (-185, -255), (-185, -330)]

  print(guessArray,'-',  attempt)
  
  new_coords = coords[attempt]
  print(new_coords)

  tr.penup()
  turtle.goto(new_coords)
  tr.pendown()

  for i in range(len(guessArray)):
    guessArray[i] = guessArray[i].upper()
  
  print(guessArray)

  for letter in guessArray:
    tr.pendown
    letterWrite = letter
    turtle.write(letterWrite, font=("sans serif", 20, "normal"))
    turtle.penup()
    turtle.forward(75)

def ChooseWord(): 
#out of 1 - 5757
  LineNum = random.randint(1,5757)

  f = open('/Users/henryburbridge/Desktop/Computer Science/Programming/Python/Projects/Wordle/words.txt')
  lines = f.readlines()
  
  wordle = lines[LineNum]
  print(wordle)
  return(wordle)

wordle = ChooseWord()
attempt = 0
line = 0


def write() : 
  
  global attempt 

  while attempt != 5:
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
  global attempt
  values = []
  check = 0
  guess_array = list(guess)
  wordle_array = list(wordle)
  
  while check != 5:
    cmpGuess = guess_array[check]
    cmpWordle = wordle_array[check]
  

    if cmpGuess == cmpWordle:
      print("Letter", check + 1, "is Green")
      values.append(2)
      drawBox('Green')

    elif cmpGuess in wordle_array:
      print("Letter", check + 1, "is Yellow")
      values.append(1)
      drawBox('Yellow')


    else:
      print("Letter", check + 1, "is Black")
      values.append(0)
      drawBox("Black")

  
    check = check + 1
  
  newLine(attempt + 1)
  turtleLetters(guess_array, attempt)
  return(values)

write()



