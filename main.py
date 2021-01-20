# MADE BY: Lisette Spalding
# FILE NAME: main.py
# DATE CREATED: 01/14/2021
# DATE LAST MODIFIED: 01/20/2021

######### IMPORTS #########
from tkinter import *
from tkinter import font as font
########### FIN ###########

### Setting up GUI window ###
root = Tk() # Every Tkinter project needs this
root.title("First GUI!")
root.geometry("400x400") # Setting the frame (window) height and width
root.configure(bg = "#e83ac5")
root.attributes("-fullscreen", False)

frame = Frame(root) # Setting the second frame up
frame.grid()

# LABEL STUFF #
# Label One
lblfnt0 = font.Font(family="Chiller",size=32,weight="bold")
lbl0 = Label(frame, text="This is the best label ever...", font=lblfnt0, bg="#bbdb1a", \
            fg = "#3103fc")
lbl0.grid() # Putting the label on the grid

# Label Two
lblfnt1 = font.Font(family="fixedsys",size=25,weight="bold")
lbl1 = Label(frame, text="A label... Spotted in the wild...", font=lblfnt1, bg="#bbdb1a", \
            fg = "#3103fc")
lbl1.grid()
## LABEL FIN ##

# BUTTON STUFF #
bttn1 = Button(frame, text="Do NOT Click!!!!!!!!")
bttn1.grid()

bttn2 = Button(frame)
bttn2.config(text = "Really DO NOT CLICK!!!!!!!!!!")
bttn2.grid()

bttn3 = Button(frame)
bttn3.grid()
bttn3["text"] =  "Fine... Click it..." # This one uses something called a dictionary to define the text
## BUTTON FIN ##

keys={"favColor":"Red","favFood":"pizza"} # Setting up a dictionary
favlbl = Label(frame,text=keys["favColor"])
favlbl.grid()

# TEN BUTTONS 3 LINES....
for i in range(10):
    bttn10 = Button(frame, text="Button "+str(i+1))
    bttn10.grid()

root.mainloop()
############ FIN ############