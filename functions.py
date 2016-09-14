# File containing different functions for certain aspects of the assignment. Just code whatever part of the assignment you want to and we can throw the code pieces together later on in main.py

"""
-----------------
  DEPENDANCIES
-----------------
"""

import turtle # For testing

import random
import math
import ScoreBoard


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

"""
-----------
  GLOBALS
-----------
(These are the global variables used in this module. Ideally we want to keep these to as few as possible)


- theta (the angle between the starting point, which is rendered dynamically, and either of the goal posts)

- x_spot (the x-co-ordinate of place marked 'X' where the ball is kicked/shot from')

- start_point (the full co-ordiantes (x,y) of point marked 'X' where the ball is kicked/shot from', it uses x_spot as the first co-ordinate and line_height//2 for the second, so Start_point = (x_spot, line_height//2))

- r (the hypotenuse, think Theorem of Pythagoras, of the triangle formed by vertices start_point, line_height//2 and the top/bottom of the goal posts, used for trigonometric calculations run in function 'projection' and in 'graphics' to draw dashed line

- x_distance (the horizontal distance from start point 'X' to line, used in trigonometric calculations in functions 'projection' and in 'graphics')

"""
start_point = (0, 0)
x_spot = 0
theta = 0
r = 0
x_distance = 0
saves = 0
goals = 0

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def setRandomPos(line):
    """
    @Outline: 
    Positions the 'Goalie' turtle randomly along the goal line

    @Parameters: 
        line - line object defined in main.py, essentially a 3-tuple (x, y, height)
    """
    return (line[0], random.randrange(line[1], line[1]+line[2]))

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
def draw_line(window, turtle, width):
    """
    @Parameters: 
        window - denotes Turtle.Screen() object
        turtle - denotes turtle object
        width - denotes width of line
    """
    
    # Data needed to draw line
    screensize = window.screensize()
    x = -(screensize[0]//1.25)
    y = -(screensize[1]//2) 
    line_height = screensize[1]
    """
    NOTE : This function draws the line dynamically based on the screensize, 
    the '1.25' and '2' are just scaling constants to position the turtle to draw the line 
    based on the screensize   
    """
    
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

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
def projection(line):
    #@Outline: This function calculates the projected impact position of the ball from a random angle. Just uses some basic trigonometry to calculate projected impact position from randomly generated angle
    global theta
    global r
    global x_distance
    """
    #@Params: 
     - theta (angle between starting point to either top of goal post or bottom of goal post)
     - r (hypotenuse calculated for triangle formed by dashed line, 'X' and middle of goal post)
    """
    # Generating random angle in range (-a, a):
    angle = random.uniform(theta*-1, theta)
        
    # Projecting onto line
    y = r*math.sin(angle)
    x = line[0]
    
    # Hypotenuse of Impact Triangle
    hyp = math.sqrt(y**2 + x_distance**2)
    
    return [(x, y), angle, hyp]
   
   # Returns projected (exact) impact position on line and angle
   # Returns angle if needed (later on)
   
   
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

"""
------
  AI 
------

This is where the main portion of the AI is housed.

"""

def orient_turtle(turtle, impact_pos):
    """
    This function orients the turtles to the projected impact position
    """
    turtle.setheading(0)
    turtle.left(turtle.towards(impact_pos))
    
def update_goal_counter(ball, ball_distance, keeper_distance, ball_speed, keeper_speed):
    """
    This function updates the goal counter and makes the scoreboard visible
    """    
    # time = distance/speed
    global goals
    global saves
    time_ball = ball_distance/ball_speed
    time_keeper = keeper_distance/keeper_speed
    if (time_ball > time_keeper):
        saves += 1
        ScoreBoard.counter_label("SAVE!!!")
    else:
        goals +=1
        ScoreBoard.counter_label("GOAL!!!")
 
def keeper_or_ball_first(ball, ball_distance, keeper_distance, ball_speed, keeper_speed):
    """
    This function is used purely to calculate wheter the keeper or ball arrives at the impact position first
    """        
     # time = distance/speed
    time_ball = ball_distance/ball_speed
    time_keeper = keeper_distance/keeper_speed
    if (time_ball > time_keeper):
        return('keeper-arrives-first')
    else:
        return('ball-arrives-first')
             
def simulation(window, ball, keeper, line, ball_speed, keeper_speed):
    """
    Outline: This is the main function, it houses the whole simulation
    
    @Params:
    window - The TurtleScreen()
    ball - The turtle representing the ball
    keeper - The turtle representing the keeper
    line - The line object drawn initially in main.py
    ball_speed - The speed of the ball (in pixels.iteration^{-1})
    keeper_speed - The speed of the keeper (in pixels.iteration^{-1})
    
    Important Note: Speed is defined in this simulation as the number of pixels moved per iteration of a loop. In a real-world environment speed would be m/s (metres per second), but for this simulated environment speed is defined as pixels/iteration, therefore a speed with magnitude 10, implies that a turtle will move 10 pixels for each iteration (each iteration of the while loop)
    
    """
    # Speed def= pixels.iterations^{-1} 
    # Because of this definition of speed, the error distance will be +- the speed (in pixels)
    global start_point
    global saves
    global goals
    
    # Getting Projection Data
    projection_data = projection(line)
    impact_position = projection_data[0]
    angle = projection_data[1]
    
    # Setting Speed of Turtles
    ball.speed(ball_speed)
    keeper.speed(keeper_speed)
       
    # Getting ball 'turtle' ready
    ball.penup()
    ball.width(3)
    ball.setpos(start_point)
    
    #Setting ball 
    window.register_shape('./images/soccer_ball.gif')
    ball.shape('./images/soccer_ball.gif')    
           
    # Orienting turtles
    orient_turtle(ball, impact_position)
    orient_turtle(keeper, impact_position) 
    
    # Moving Turtles
    ball_distance = projection_data[2] # Distance ball has to travel
    keeper_distance = math.fabs(impact_position[1] - keeper.pos()[1])
    
    # Initializing counters to keep track of distances
    ball_distance_counter = ball_distance
    keeper_distance_counter = keeper_distance

    # Creating Text Turtle
    text_turtle = turtle.Turtle()
    text_turtle.shape('blank')  
    text_turtle.penup() 
         
    # Speed def= pixels.iterations^{-1} 
    # Because of this definition of speed, the error distance will be +- the speed (in pixels)
    ball_arrived = False
    keeper_arrived = False
    
    while(ball_arrived == False): #This way one (and most often ONLY one turtle) will always reach the impact position, iterations are the analogue of time 
        
        # Moving Ball
        
        ball.pencolor('grey')
        ball.pendown()
        
        if ((ball_distance_counter - ball_speed/2) > 0.0): # If this is true, the ball still has space to move forward to impace position
            # Ball Movement
            ball.forward(ball_speed/2)
            text_turtle.clear()
            text_turtle.setpos(ball.pos())    
            # Text
            text_turtle.write('Impact Position: {}'.format(impact_position))
            # Updating Counter
            ball_distance_counter -= ball_speed/2
            
        elif(keeper_or_ball_first(ball, ball_distance, keeper_distance, ball_speed, keeper_speed) == 'ball-arrives-first'): # Checking to see if the ball arrives first via calculations
            ball.speed(ball_speed) # We have to do this as the error distance is dependant on the speed
            ball.goto(impact_position) # We have to do this as the error distance is dependant on the speed
            ball_arrived = True
            
        ball.penup()
        
        if ((ball_distance_counter - ball_speed/2) > 0.0): # If this is true, the ball still has space to move forward to impace position
            ball.forward(ball_speed/2)
            ball_distance_counter -= ball_speed/2   
            
        elif(keeper_or_ball_first(ball, ball_distance, keeper_distance, ball_speed, keeper_speed) == 'ball-arrives-first'):
            ball.speed(ball_speed) # We have to do this as the error distance is dependant on the speed
            ball.goto(impact_position) # We have to do this as the error distance is dependant on the speed
            ball_arrived = True
            
        # Moving Keeper
        
        if ((keeper_distance_counter - keeper_speed) > 0.0):
            keeper.forward(keeper_speed)            
            keeper_distance_counter -= keeper_speed
            
        if (((ball_distance_counter - ball_speed/2) < 0.0) and ((keeper_distance_counter - keeper_speed) < 0.0)):
            # This branch will be reached if the keeper arrives first and the ball arrives second
            keeper.setpos(impact_position) # We have to do this as the error distance is dependant on the speed
            ball.setpos(impact_position)
            ball_arrived = True
    
    # Updating Goal Counter        
    update_goal_counter(ball, ball_distance, keeper_distance, ball_speed, keeper_speed)
    ball.goto(0,0)

    
def generate_random_speed():
    values=[0.5,0.25,1.25,1.75,2]
    # variable s= the speed of the Goalie
    s=random.randrange(1,10)  
    # so the range is 1-10, because speed works in that range of integers. I didn't include 0 because well...that means no movement. Turns out 1=fastest and 0=slowest.
    speed=(int)(s*(values[random.randrange(0,4)])) # speed of the ball
    if speed > 10 or speed <0.5:
        speed=6  # 6 is seen as the 'normal' speed
    
    
    #return null
    return speed    


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


"""
------------
  GRAPHICS
------------

The 'graphics()' function draws the Playing Field and Visualisation aspects of the program


"""

def graphics(window, turtle, line, dashes):    
    global theta
    global x_spot
    global start_point
    global x_distance
    global r
    
    """
    @Parameters: 
        window - denotes Turtle.Screen() object
        turtle - denotes turtle object
        line - denotes line drawn
        dashes - number of dashes (change this in main.py if you want to)
    """
    
    # Drawing initial x
    y = line[2]//2
    screensize = window.screensize()
    x_spot = (screensize[0]//1.25)
    turtle.shape('blank')
    turtle.penup()
    turtle.setpos(x_spot, line[1] + y)
    turtle.width(20)
    window.register_shape('./images/x_spot.gif')
    turtle.shape('./images/x_spot.gif')
    turtle.stamp()
    
    # Setting start point
    start_point = (x_spot, line[1] + y)
    
    
    turtle.shape('blank') # Resetting 'shape' property to default
    # Drawing Upper Dotted Line
    x_distance = x_spot - line[0]    
    theta = math.atan(y/x_distance)
    turtle.left(math.degrees(math.pi-theta))
    
    r = math.sqrt(x_distance**2 + y**2)
    turtle.width(5)
    turtle.pencolor('#183720')
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
 
def getGoals():    
    global goals
    return goals

def getSaves():    
    global saves
    return saves   
