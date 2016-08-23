# File containing different functions for certain aspects of the assignment. Just code whatever part of the assignment you want to and we can throw the code pieces together later on in main.py

import random
import math


def setRandomPos(line):
    #@Parameters: 
        # line - line object defined in main.py, essentially a 3-tuple (x, y, height)
    return (line[0], random.randrange(line[1], line[1]+line[2]))
    

def draw_line(window, turtle, width):
    #@Parameters: 
        # window - denotes Turtle.Screen() object
        # turtle - denotes turtle object
        # width - denotes width of line
    
    # Data needed to draw line
    screensize = window.screensize()
    x = -(screensize[0]//1.25)
    y = -(screensize[1]//2) 
    line_height = screensize[1]
    #NOTE : This function draws the line dynamically based on the screensize, 
        #the '1.25' and '2' are just scaling constants to position the turtle to draw the line 
        #based on the screensize    
    
    # Drawing Line
    turtle.shape('blank')
    turtle.penup()
    turtle.setpos(x,y)
    turtle.left(90)
    turtle.pendown()
    turtle.width(width)
    turtle.forward(line_height)
    turtle.penup()    
    
    # Returning the co-ordinates of the starting point of the line <x,y> and the line height.
    # We need this info returned here to determine the range in which the 'Goalie' turtle can spawn.
    return (x, y, line_height)
    


def graphics(window, turtle, line, dashes):
    #@Parameters: 
        # window - denotes Turtle.Screen() object
        # turtle - denotes turtle object
        # line - denotes line drawn
        # dashes - number of dashes (change this in main.py if you want to)
    
    # Drawing initial x
    y = line[2]//2
    screensize = window.screensize()
    x_spot = (screensize[0]//1.25)
    turtle.shape('blank')
    turtle.penup()
    turtle.setpos(x_spot, line[1] + y)
    turtle.width(20)
    turtle.shape('turtle')
    turtle.stamp()
    
    
    turtle.shape('blank') # Resetting 'shape' property to default
    # Drawing Upper Dotted Line
    x_distance = x_spot - line[0]    
    theta = math.atan(y/x_distance)
    turtle.left(math.degrees(math.pi-theta))
    
    r = math.sqrt(x_distance**2 + y**2)
    turtle.width(1)
    #Drawing Dashes ------
    for i in range(dashes):
        turtle.pendown()
        turtle.forward((r/dashes)/2)     
        turtle.penup()  
        turtle.forward((r/dashes)/2)
    
    
    # Drawing Lower Dotted Line
    turtle.setpos(x_spot, line[1] + y)
    turtle.towards(x_spot, line[1] + y)
    turtle.left(math.degrees(2*theta))
    #Drawing Dashes ------
    for i in range(dashes):
            turtle.pendown()
            turtle.forward((r/dashes)/2)     
            turtle.penup()  
            turtle.forward((r/dashes)/2)    
    