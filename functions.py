# File containing different functions for certain aspects of the assignment. Just code whatever part of the assignment you want to and we can throw the code pieces together later on in main.py

import random

def random_starting_position(x, turtle, line_start, line_finish):
    #@Parameters: 
        # x - denotes position of line along x-axis
        #turtle - denotes turtle object
        #line_start - y co-ordinate at start of line
        #line_finish - y co-ordinate at end of line
    turtle.setpos(x, random.randrange(line_start, line_finish))
    

def draw_line(window, turtle, width):
    #@Parameters: 
        # vector (x,y) - denotes starting position of line
        # turtle - denotes turtle object
        # height - denotes height of line
    screensize = window.screensize()
    x = -(screensize[0]//1.25)
    y = -(screensize[1]//2) 
    turtle.penup()
    turtle.setpos(x,y)
    turtle.left(90)
    turtle.pendown()
    turtle.width(width)
    turtle.forward(screensize[1])
    turtle.penup()    
    #NOTE : This function draws the line dynamically based on the screensize, 
    #the '1.25' and '2' are just scaling constants to position the turtle to draw the line 
    #based on the screensize
    

    

    