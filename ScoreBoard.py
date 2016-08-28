import tkinter as tk       #Basically importing the python gui function: tkinter
import time #used for the timer added

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

def counter_label(temp, score):  
    root = tk.Tk() # Creates a  separate window i.e. the label that should display 
    root.title("Score Board Update") #Title
    label = tk.Label(root,  fg="blue", font="Times") # customise defined label
    label.pack() # this sort of adjusts the windows size based on the labels contents  
    center(root)  
  
    def delete():           
        label.configure(text = ("The score is", str(score)), bg = "orange")
        root.configure(bg = "orange")

    def destroy():    
        root.destroy()
    
    if temp == "GOAL!!!":        
        label.configure(bg = "red")
        root.configure(bg = "red")
  
    if temp == "SAVE!!!":    
        label.configure(bg = "green")
        root.configure (bg = "green")
  
    label.configure(text = temp)
    label.after(2000, delete)
    label.after(5000, destroy)
  

