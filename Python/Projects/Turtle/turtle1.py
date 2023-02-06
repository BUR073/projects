# library usually installed by default with python
import turtle
import time
x = 0
y = 1

turtle.color("blue")
x = 0
y = 0
t = turtle.Turtle()

t.hideturtle()

turtle.speed(0)




def move():
    t.penup()
    t.forward(200)
    t.pendown()

def square_func():
    square = [ (0, 100), (100, 100), (100, 0), (0, 0) ]
    t.color("red")
    for coord in square:
            t.goto(coord[x], coord[y])
        
    

def diamond_func():
    diamond = [ (0, 0), (-45, 75), (0, 110), (45, 75), (0, 0)]
    t.color("green")
    for coord in diamond:
        t.goto(coord[x], coord[y])

    

def rhombus_func():
    rhombus = [ (0, 0), (25, 100), (125, 100),(100, 0), (0, 0)]
    t.color("hot pink")
    for coord in rhombus:
        t.goto(coord[x], coord[y])

def go():
    square_func()
    
    rhombus_func()
    print("Rhombus")
    move()
    print("Moving...")
    diamond_func()
   
    print("Diamond")
    move()
    print("Moving...")
    rhombus_func()

    print("Rhombus")





 

go()



##x = 0
##a = 1
##
##
##
##shape = [square, diamond, rhombus]
##for i in shape:
##    
##    shape_type = i
##    
##    for coord in shape_type:
##        while a < (len(shape_type)):
##            t.goto(coord[x], coord[y])
##            a = a - 1
##            print(len(shape_type))
##
##            if a == 0:
##                move()

    

  
        


# EXERCISE

# 1. Using lines 20-23 as as a template, add a diamond shape alongside the square.

# 2. In the same way, add a rhombus.

# 3. Put your individual shapes into a list and refactor your code so that it iterates over the list of shapes and draws each shape
# 4. What extra code do you need to tidy it up?
