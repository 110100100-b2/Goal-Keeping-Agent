# File containing different functions for certain aspects of the assignment. Just code whatever part of the assignment you want to and we can throw the code pieces together later on in main.py

import random

def random_starting_position(x, turtle, line_start, line_finish):
    #@Parameters: 
        # x - denotes position of line along x-axis
        #turtle - denotes turtle object
        #line_start - y co-ordinate at start of line
        #line_finish - y co-ordinate at end of line
    turtle.setpos(x, random.randrange(line_start, line_finish))
    

def draw_line(vector, turtle, height, width):
    #@Parameters: 
        # vector (x,y) - denotes starting position of line
        # turtle - denotes turtle object
        # height - denotes height of line
    turtle.setpos(vector)
    turtle.pendown()
    turtle.width(width)
    turtle.forward(height)
    turtle.penup()
    