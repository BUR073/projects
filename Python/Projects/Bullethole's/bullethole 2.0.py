## Grouping Size
import math
import turtle

t = turtle.Turtle()
t.hideturtle()
t.speed(0)


x = 0
y = 1


coords = [(100, 200), (100, 100), (300, 400)]
t.pendown()


        

def distance(a, b):
    xDS = (b[x] - a[x]) ** 2
    yDS = (b[y] - a[y]) ** 2
    return math.sqrt( xDS + yDS)

maxDist = 0
X = 0
Y = 0

for i in range(len(coords)-1):
    for j in range(i + 1, len(coords)):
        
        newDist = distance(coords[i], coords[j])
        if newDist > maxDist:
            maxDist = newDist
            X = coords[j]
            Y = coords[i]

      


##
print("Maximum Distance:", maxDist)
print(X,",", Y)
mid_point = tuple(map(sum,zip(X,Y)))
mid_point = tuple(ti/2 for ti in mid_point)
print("Mid Point:", mid_point)
##





