import random
import turtle
import time

turtle.hideturtle()
random_1 = (random.randint(1,9))
random_2 = (random.randint(0, 360))
turtle.speed = 1000000000
turtle.tracer(0, 0)
turn1 = 1000
turn2 = 1001
turn2 = 1002
turn3 = 1003
turn4 = 1004

def circle_draw():
    x = 360 
    while x != 0:
        turtle.forward(2)
        turtle.right(1)
        x = x - 1


move = 1
while move != 1000:
    turtle.color("Hot Pink")
    turtle.circle(turn4)
  
   
    
    turtle.color("Yellow")
    turtle.circle(turn3)

  
    
    turtle.color("Green")
    turtle.circle(turn2)

  
    
    turtle.color("Blue")
    turtle.circle(turn1)
    
    turtle.right(10)
    move = move + 1
    


    turn1 -= 1
    turn2 -= 1
    turn3 -= 1
    turn4 -= 1

    print(turn1, turn2, turn3, turn4)
    
             
turtle.update()

while x == 0:
    random_1 = (random.randint(0, 5))
    random_2 = (random.randint(0, 360))
    random_turn = (random.randint(1,2))

    turtle.forward(random_1)
  

    if random_turn == 1:
        turtle.right(random_2)
       

    else:
        
        turtle.right(random_2)
##

import turtle
from turtle import Screen, Turtle

screen = Screen()
t = Turtle("turtle")
t.speed(-1)

def dragging(x, y):  # These parameters will be the mouse position
    t.ondrag(None)
    t.setheading(t.towards(x, y))
    t.goto(x, y)
    t.ondrag(dragging)

def clickRight():
    t.clear()

def main():  # This will run the program
    turtle.listen()
    
    t.ondrag(dragging)  # When we drag the turtle object call dragging
    turtle.onscreenclick(clickRight, 3)

    screen.mainloop()  # This will continue running main() 

main()
