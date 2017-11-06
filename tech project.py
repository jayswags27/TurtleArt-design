import turtle
from turtle import*
bob=turtle.Turtle()
bob.speed(0)
shape("turtle")



wheel=1
a=turtle.Screen()
bgcolor("red")
for i in range (wheel):
    ninja = turtle.Turtle()
pencolor('magenta')
ninja.speed(0)
pencolor('magenta')
for i in range(180):
    pencolor('magenta')
    ninja.forward(200)
    ninja.right(60)
    ninja.forward(40)
    ninja.left(120)
    ninja.forward(100)
    ninja.right(60)
    
    ninja.penup()
    ninja.setposition(0, 0)
    ninja.pendown()
    
    ninja.right(4)
    


    speed(0) # sets the speed of drawing to 0, which is the fastest
pencolor('cyan') # sets the color of the pen/lines to white
bgcolor('red') # sets the color of the background/canvas to black

x = 0 # creates a variable x with value 0
up() # lifts up the pen, so no lines are drawn

#note fd() means move forward, bk() means move back
# rt() or lt() means tilt right by a certain angle

rt(45) 
fd(90) 
rt(135) 

down() # sets down the pen, so that turtle can draw
while x < 120: # while the value of x is lesser than 120,
                #continuously do this:
    fd(200)     
    rt(61)
    fd(200)
    rt(61)
    fd(200)
    rt(61)
    fd(200)
    rt(61)
    fd(200)
    rt(61)
    fd(200)
    rt(61)

    rt(11.1111) 
    x = x+1 # adds 1 to the value of x,
            # so that it is closer to 120 after every loop

from designfunctions import *
gordon = turtle.Pen()

gordon.speed(0)
gordon.shape("turtle")

gordon.color("magenta")

gordon.width(3)

for i in range(200):

    gordon.forward(10*i)

    gordon.left(90)








