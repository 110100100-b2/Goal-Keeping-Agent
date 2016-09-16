import tkinter as tk       #Basically importing the python gui function: tkinter
import time                #used for the timer added
import functions

goals = 0 
saves = 0

def center(root): #to center our roots
    root.update_idletasks() # to ensure accuracy in height and width values
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    geo = root.geometry()
    size = tuple(geo.split('x'))
    size2 = tuple(size[1].split('+'))
    
    x = width/2 - int(size[0])/2
    y = height/2 - int(size2[0])/2
    root.geometry("%dx%d+%d+%d" % ((int(size[0]), int(size2[0])) + (x, y)))

def start_or_quit(temp):    #start and quit roots
    global goals
    global saves
    
    def findGoalsToShotsRatio(goals, saves): #finds simplest goals to shots ratio
        
        shots = goals + saves
        val = 1

        for i in range(1, (shots + 1)):
               
            if goals%i == 0 and shots%i == 0:
                
                val = i
        
        return (str(goals/val) + ":" + str(shots/val))
       
    
    root = tk.Tk() #creating root
    root.title("Instructions")
    root.configure(bg = "orange")
    
    if temp == "START":        
        temp = "'Space' to shoot\n'i' for help\n'c' to clear dotted shot lines\n'q' to quit"    
    elif temp == "QUIT":        
        temp = ("Total Goals - " + str(goals) + "\nTotal Shots - " + str((goals + saves)) + "\nTotal Saves - " + str(saves) + "\nGoals-Shots Ratio - " + findGoalsToShotsRatio(goals, saves) + "\nAverage Ball Speed - " + str(round(functions.getAverageBallSpeed(), 2)))
        
    label = tk.Label(root, fg = "blue", font = "Times", bg = "orange", text = temp)
    label.pack()
    center(root)
    
    label.after(5000, root.destroy) #deletes root after 5 seconds
    

def counter_label(temp): #appears after every shot
    global goals
    global saves
    goals = functions.getGoals()
    saves = functions.getSaves()
    
    root = tk.Tk() # Creates a  root 
    root.title("Score Board Update") #Title
    label = tk.Label(root,  fg="blue", font="Times") # customise defined label
    label.pack()
    center(root)  
  
    def delete():           
        label.configure(text = (str(goals) + " goal(s) scored"), bg = "orange")
        root.configure(bg = "orange")
        label.pack()
    
    if temp == "GOAL!!!":        
        label.configure(bg = "red")
        root.configure(bg = "red")
  
    if temp == "SAVE!!!":    
        label.configure(bg = "green")
        root.configure (bg = "green")

  
    label.configure(text = temp)
    label.pack() # this sort of adjusts the windows size based on the labels contents 
    label.after(2000, delete)
    label.after(5000, root.destroy)
  



