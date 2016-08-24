# Main Program can go here, we can load all other modules and run it in this .py file.

import turtle
import functions

wn = turtle.Screen()
wn.title("Goal Keeping Agent")
wn.bgcolor("lightgreen")
wn.bgpic(r"back.gif")

# Creating Goalie Turtle Object
goalie = turtle.Turtle()

#Creating Ball
ball = turtle.Turtle()
ball.shape('blank')    
    


# We use this to determine the range which the Goalie can randomly appear
line = functions.draw_line(wn, goalie, 5)

#Essentially what this is doing is determining a random y value that lies along the line x = line[0], thus we can determine a random position <x, y> that will ALWAYS be along the line we've drawn
goalie.setpos(functions.setRandomPos(line))
goalie.shape('circle')

#Drawing Visualisation
graphicsTurtle = turtle.Turtle()
functions.graphics(wn, graphicsTurtle, line, 50)


def shoot():
    #functions.shoot(wn, ball, line, 2)
    #functions.react(wn, goalie, line, 1)
    functions.engine(wn, ball, goalie, line, 2, 1)

wn.onkey(shoot, "space")

wn.listen()
wn.mainloop()
