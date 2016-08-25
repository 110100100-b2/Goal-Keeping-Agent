

import tkinter as tk       #Basically importing the python gui function: tkinter
import time #used for the timer added

score = 0

def counter_label(label):
  def count():
    global score
    
    score += 1
    
    label.config(text=str(score))
    
  count()
 
 
root = tk.Tk() # Creates a  separate window i.e. the label that should display 
root.title("Score Board Update") #Title

label = tk.Label(root,  fg="blue", font="Times") # customise defined label
label.pack() # this sort of adjusts the windows size based on the labels contents
counter_label(label)

def score(temp): #momentarily informs the user whether a goal or save occured
  
  def delete(): #used to clear the label 
    
    label.configure(text = "1", bg = "white")
  
  if temp == "GOAL!!!":
    
    label.configure(bg = "red") 
                     
  if temp == "SAVE!!!":
    
    label.configure(bg = "green")
  
  label.config(text = temp)  
  label.after(2000, delete)

root.mainloop()
