import tkinter as tk       #Basically importing the python gui function: tkinter
import time #used for the timer added
 
root = tk.Tk() # Creates a  separate window i.e. the label that should display 
root.title("Score Board Update") #Title

label = tk.Label(root,  fg="blue", font="Times") # customise defined label
label.pack() # this sort of adjusts the windows size based on the labels contents

def counter_label(temp, score):
  
  def delete():
    
    label.configure(text = ("The score is", str(score)), bg = "white")
  
  def destroy():
    
    root.destroy()
    
  if temp == "GOAL!!!":
    
    label.configure(bg = "red")
  
  if temp == "SAVE!!!":
    
    label.configure(bg = "green")
  
  label.configure(text = temp)
  label.after(2000, delete)
  label.after(5000, destroy)

counter_label("GOAL!!!", 2)
root.mainloop()
