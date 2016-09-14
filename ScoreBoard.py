import tkinter as tk       #Basically importing the python gui function: tkinter
import time #used for the timer added
import functions

goals = 0
saves = 0

def center(root):
    root.update_idletasks() # to ensure accuracy in height and width values
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    geo = root.geometry()
    size = tuple(geo.split('x'))
    size2 = tuple(size[1].split('+'))
    
    x = width/2 - int(size[0])/2
    y = height/2 - int(size2[0])/2
    root.geometry("%dx%d+%d+%d" % ((int(size[0]), int(size2[0])) + (x, y)))

def start_or_quit(temp):    
    global goals
    global saves
    
    root = tk.Tk()
    root.title("Instructions")
    root.configure(bg = "orange")
    
    if temp == "START":        
        temp = "'Space' to shoot\n'i' for help\n'c' to clear dotted shot lines\n'q' to quit"    
    elif temp == "QUIT":        
        temp = ("Total Goals - ", goals, "\nTotal Shots - ", (goals + saves), "\nTotal Saves - ", saves)
        
    label = tk.Label(root, fg = "blue", font = "Times", bg = "orange", text = temp)
    label.pack()
    center(root)
    
    def destroy():        
        root.destroy()
    
    label.after(5000, destroy)
    

def counter_label(temp): 
    global goals
    global saves
    goals = functions.getGoals()
    saves = functions.getSaves()
    
    root = tk.Tk() # Creates a  separate window i.e. the label that should display 
    root.title("Score Board Update") #Title
    label = tk.Label(root,  fg="blue", font="Times") # customise defined label 
    center(root)  
  
    def delete():           
        label.configure(text = ("The score is ", goals), bg = "orange")
        root.configure(bg = "orange")
        label.pack()

    def destroy():    
        root.destroy()
    
    if temp == "GOAL!!!":        
        label.configure(bg = "red")
        root.configure(bg = "red")
  
    if temp == "SAVE!!!":    
        label.configure(bg = "green")
        root.configure (bg = "green")

  
    label.configure(text = temp)
    label.pack() # this sort of adjusts the windows size based on the labels contents 
    label.after(2000, delete)
    label.after(5000, destroy)
  



