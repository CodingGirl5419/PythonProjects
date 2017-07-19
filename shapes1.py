from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
setup(500,300)
#x_pos = -250
#y_pos = -150
#
### Write your code below:
inp = int(input("How many sides?"))

def shape(num):
    for i in range(num):
        t.forward(90)
        t.left(360/num)

shape(inp)




#def shape(num):
    #for i in range(num):
        #t.forward(90)
        #t.left(360/num)

#shape(5)
#shape(3)

pendown()
pencolor("red")
forward (90)
pencolor("purple")
left (60)
pencolor("green")
back (90)
pencolor("pink")
left (60)
pencolor("yellow")
forward (90)
pencolor("brown")


# Close window on click.
exitonclick()
