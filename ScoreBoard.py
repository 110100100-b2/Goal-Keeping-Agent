

import tkinter as tk       #Basically importing the python gui function: tkinter

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

root.mainloop()