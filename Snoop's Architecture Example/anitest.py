import turtle 
import random
from math import ceil

#turtle.setup(600, 600)
wn = turtle.Screen()
wn.title("Robocup demo")
wn.bgcolor("lightgreen")

ball = turtle.Turtle()
ball.penup()
ball.shape("circle")
ball.shapesize(2)
ball.fillcolor("white")
ball.speed("fastest")
ball.setheading(180)

goalie = turtle.Turtle()
goalie.penup()
goalie.shape("circle")
goalie.shapesize(2)
goalie.fillcolor("red")
goalie.speed("fastest")
goalie.setheading(90)
goalie.goto(-300, 0)

def doNothing():
    return

def aim():
    wn.onkey(doNothing, "space")
    ball.home()
    ball.setheading(180)
    angle = random.randrange(0, 46)
    direction = random.randrange(0,2)
    if direction == 0: # left
        ball.left(angle)
    else:
        ball.right(angle)
    shoot()

def shoot():
    goalieStep = 2
    #print("b {0}, g {1}".format(ceil(ball.position()[1]), ceil(goalie.position()[1])))
    if ball.position()[0] <= -300:
        if ceil(goalie.position()[1]) == ceil(ball.position()[1]):
            goalie.write("save")
        else:
            ball.write("score")
        wn.ontimer(doNothing)
        wn.onkey(aim, "space")
    else:
        # Insert AI logic here
        goalie.forward(goalieStep)
        ball.forward(4)
        wn.ontimer(shoot, 100)

wn.onkey(aim, "space")
wn.listen()
wn.mainloop()


