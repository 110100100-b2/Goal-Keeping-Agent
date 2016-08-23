# Main Program can go here, we can load all other modules and run it in this .py file.

import turtle
import functions

wn = turtle.Screen()
wn.title("Goal Keeping Agent")
wn.bgcolor("lightgreen")

# Creating Goalie Turtle Object
goalie = turtle.Turtle()

# We use this to determine the range which the Goalie can randomly appear
line = functions.draw_line(wn, goalie, 5)

#Essentially what this is doing is determining a random y value that lies along the line x = line[0], thus we can determine a random position <x, y> that will ALWAYS be along the line we've drawn
goalie.setpos(functions.random_starting_position(line[0], line[1], line[1]+line[2]))
goalie.shape('circle')
#NOTE:
# -line[0] = x co-ordinate of starting position of line
# -line[1] = y co-ordinate of starting position of line
# -line[2] = height of line
# I'll simplify this code a bit later on


wn.listen()
wn.mainloop()