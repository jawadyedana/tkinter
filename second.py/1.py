# Import neccessary libaries
from tkinter import * # IMPORT EVERYTHING 
from tkinter import messagebox # import msgbox

# setup tkinter window 
root = Tk()
root.title("first window")
root.geometry("400x400")

def msg():
    #                       title,  text
    messagebox.showwarning("Alert", "stop! virus found.")

# widget
button = Button(root, text="scan for virus", command=msg)
button.place(x=40, y=80) # position it x => horzontal value, y => vertical value

root.mainloop()