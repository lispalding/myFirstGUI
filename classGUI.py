# MADE BY: Lisette Spalding
# FILE NAME: main.py
# DATE CREATED: 01/20/2021
# DATE LAST MODIFIED: 01/20/2021

######### IMPORTS #########
from tkinter import *
from tkinter import font as font
########### FIN ###########

########### CLASSES ###########
class App(Frame):
    """ To use: App(root)
    This is a class that will build a clicker app. """
    def __init__(self,master): # Defining the "in it" class for App()
        super(App, self).__init__(master) # Labeling it as a master class
        self.grid()
        self.clicks = 0
        self.colors = ["red","blue","green", "yellow"]
        self.colorIndex = 0
        self.bttnIndex = 1
        self.createWidgets()

    def createWidgets(self):
        """ To use: createWidgets()
        This method creates widgets for the app. In the window. """
        ### Labels
        self.lblTotal = Label(self, text="Total Clicks: ")
        self.lblNumClicks = Label(self, text=str(self.clicks))

        ### Buttons
        self.addBttn = Button(self, text="Add to count")
        self. minBttn = Button(self, text="Subtract from count")
        self. colorBttn = Button(self, text="Change color")

        ## Button Configurations
        # Style configurations
        self.addBttn.config(width=28)
        self.colorBttn.config(width=28)
        self.minBttn.config(width=28)

        # Command Configuration
        self.addBttn["command"] = self.addToCount
        self.minBttn["command"] = self.subtractFromCount
        self.colorBttn["command"] = self.changeColor

        ## Placing buttons and all that on the grid
        self.colorBttn.grid()
        self.lblTotal.grid()
        self.lblNumClicks.grid()
        self.addBttn.grid()
        self.minBttn.grid()

    def addToCount(self):
        """ To use: addToCount()
         This is a method that adds to the count."""
        self.clicks += 1

        self.lblNumClicks.config(text=str(self.clicks))

    def subtractFromCount(self):
        """ To use: subtractFromAccount()
         This is a method that subtracts from the click count."""
        if self.clicks > 0:
            self.clicks -= 1
        else:
            pass

        self.lblNumClicks.config(text=str(self.clicks))

    def changeColor(self):
        """ To use: changeColor()
         This is a method that will change the background color"""
        self.colorIndex += 1
        self.bttnIndex = self.colorIndex+1

        if self.colorIndex > len(self.colors)-1:
            self.colorIndex = 0

        if self.bttnIndex > len(self.colors)-1:
            self.bttnIndex = 0

        self.config(bg=self.colors[self.colorIndex])

        self.colorBttn.config(bg = self.colors[self.bttnIndex])

############# FIN #############

### Setting up GUI window ###
root = Tk() # Every Tkinter project needs this
root.title("First GUI!")
root.geometry("400x400") # Setting the frame (window) height and width
root.attributes("-fullscreen", False)
############ FIN ############

app = App(root)

root.mainloop() # Calling up the window...