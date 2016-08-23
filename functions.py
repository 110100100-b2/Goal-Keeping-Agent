# File containing different functions for certain aspects of the assignment. Just code whatever part of the assignment you want to and we can throw the code pieces together later on in main.py

import random

def random_starting_position(x, line_start, line_finish):
    #@Parameters: 
        # x - denotes position of line along x-axis
        #line_start - y co-ordinate at start of line
        #line_finish - y co-ordinate at end of line
    return (x, random.randrange(line_start, line_finish))
    

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
    

    

    