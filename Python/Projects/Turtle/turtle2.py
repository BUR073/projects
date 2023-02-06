
import turtle

t = turtle.Turtle()

t.hideturtle()

t.speed(0)



t.color("blue")


x = 0
y = 1



square = [(0,0), (0, 100), (100, 100), (100, 0), (0,0) ]

rhombus = [ (-100, -100), (-125, 0), (-125, 0),(0, -100), (-100, -100)]
diamond = [ (100, 100), (55, 175), (100, 210), (145, 175), (100, 100)]

shapes = [rhombus, diamond, square]
t.up()
for a in shapes:

    
  
    for coord in a:
 
        t.goto(coord[x], coord[y])
        t.down()
      
  

  
  

