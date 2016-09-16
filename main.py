# Main Program can go here, we can load all other modules and run it in this .py file.

import turtle

# Importing Modules
import sys
sys.path.insert(0, './modules')

import functions
import ScoreBoard

start = False

wn = turtle.Screen()
wn.setup(width=839, height=1039, startx = 250, starty = 0)
wn.title("Goal Keeping Agent")
wn.bgcolor("lightgreen")
wn.bgpic('./images/back.gif')
ScoreBoard.start_or_quit("START")

#Registering outside emoji shapes
wn.register_shape('./images/emojis/sleeping.gif')
wn.register_shape('./images/emojis/happy.gif')
wn.register_shape('./images/emojis/lol.gif')
wn.register_shape('./images/emojis/sad.gif')

# Creating text file to write 
functions.create_text('simulation_data.txt')

# Creating Goalie Turtle Object
goalie = turtle.Turtle()

#Creating Ball
ball = turtle.Turtle()
ball.shape('blank')  

# We use this to determine the range which the Goalie can randomly appear
line = functions.draw_line(wn, goalie, 5)

#Essentially what this is doing is determining a random y value that lies along the line x = line[0], thus we can determine a random position <x, y> that will ALWAYS be along the line we've drawn
goalie.setpos(functions.setRandomPos(line))

#Setting emoji as goalie
goalie.shape('circle') #this allows the goalkeeper's face to appear above the goal line
goalie.shape('./images/emojis/sleeping.gif') 

#Drawing Visualisation
graphicsTurtle = turtle.Turtle()
functions.graphics(wn, graphicsTurtle, line, 25)

def shoot():
    global start
    start_point = functions.getStartPoint()
    if ball.position() == start_point or start == False:        
        start = True
        functions.simulation(wn, ball, goalie, line, functions.generate_random_speed(), 1)    
    
    
def help():    
    ScoreBoard.start_or_quit("START")
    
def quit():    
    ScoreBoard.start_or_quit("QUIT")
    wn.bye()

def clearLines():    
    ball.clear()

wn.onkey(shoot, "space")
wn.onkey(help, "i")
wn.onkey(clearLines, "c")
wn.onkey(quit, "q")

wn.listen()
wn.mainloop()
