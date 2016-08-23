# File containing different functions for certain aspects of the assignment. We 

import random

def random_starting_position(x, turtle, line_start, line_finish):
    #@Parameters: 
    # x - denotes position of line along x-axis
    # turtle - denotes turtle object
    # line_start - y co-ordinate at start of line
    # line_finish - y co-ordinate at end of line
    turtle.setpos(x, random.randrange(line_start, line_finish))
    

