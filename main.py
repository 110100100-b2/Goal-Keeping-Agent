# Main Program can go here, we can load all other modules and run it in this .py file.

import turtle
import functions

wn = turtle.Screen()
wn.title("Goal Keeping Agent")
wn.bgcolor("lightgreen")

# Creating Goalie Turtle Object
goalie = turtle.Turtle()

functions.draw_line((0,0), goalie, 100, 5)


wn.listen()
wn.mainloop()