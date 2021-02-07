# MADE BY: Lisette Spalding
# FILE NAME: clicker_program.py
# PYTHON VER. USED: 3.8
# DATE CREATED: 01/20/2021
# DATE LAST MODIFIED: 01/26/2021

######### IMPORTS #########
from tkinter import *
from tkinter import font as font
import time
from datetime import datetime
import math
########### FIN ###########

########### CLASSES ###########
class App(Frame):
    """ To use: App(root)
    This is a class that will build a clicker app. """
    def __init__(self,master): # Defining the "in it" class for App()
        super(App, self).__init__(master) # Labeling it as a master class
        self.grid() # Applying the grid-- Adding object to grid
        self.clicks = 0

        self.secCalc = self.calcSecs()
        self.tapPerSec = self.clicksPerSec()

        self.colors = ["red","blue","green", "yellow"]
        self.lblColors = ["#FF675C", "#98D90D", "#4376DE", "#FFCB30", "#24940d", "#872eb0"]

        self.colorIndex = 0
        self.lblColorIndex = 0
        self.bttnIndex = 1
        self.lblIndex = 0

        self.createWidgets()

    def createWidgets(self):
        """ To use: self.createWidgets()
        This method creates widgets for the app. In the window. """
        ### Labels
        self.lblTotal = Label(self, text="Total Clicks: ")
        self.lblNumClicks = Label(self, text=str(self.clicks))
        self.lblSecClicks = Label(self, text="Clicks Per Second: ")
        self.lblClickPerSec = Label(self, text=str(self.tapPerSec))

        ### Buttons
        self.addBttn = Button(self, text="Add to count")
        self.minBttn = Button(self, text="Subtract from count")
        self.colorBttn = Button(self, text="Change color")

        ## Button Configurations
        # Style configurations
        self.addBttn.config(width=28)
        self.colorBttn.config(width=28)
        self.minBttn.config(width=28)

        # Command Configuration
        self.addBttn["command"] = self.addToCount
        self.minBttn["command"] = self.subtractFromCount
        self.colorBttn["command"] = self.changeColor

        # After Configuration
        self.lblClickPerSec.after(1000, self.refreshClickLbl)

        ## Placing buttons and all that on the grid
        self.lblSecClicks.grid()
        self.lblClickPerSec.grid()
        self.colorBttn.grid()
        self.lblTotal.grid()
        self.lblNumClicks.grid()
        self.addBttn.grid()
        self.minBttn.grid()

    def addToCount(self):
        """ To use: self.addToCount()
         This is a method that adds to the count."""
        self.clicks += 1

        self.lblNumClicks.config(text=str(self.clicks))

        if self.clicks > 0:
            self.lblChangeColor1(self.lblNumClicks)

            self.lblChangeColor1(self.lblTotal)


    def subtractFromCount(self):
        """ To use: self.subtractFromAccount()
         This is a method that subtracts from the click count."""

        if self.clicks > 0:
            self.clicks -= 1
        else:
            pass

        self.lblNumClicks.config(text=str(self.clicks))

        if self.clicks > 0:
            self.lblChangeColor2(self.lblNumClicks)

            self.lblChangeColor2(self.lblTotal)

    def changeColor(self):
        """ To use: self.changeColor()
         This is a method that will change the background color"""
        self.colorIndex += 1
        self.bttnIndex = self.colorIndex+1

        if self.colorIndex > len(self.colors)-1:
            self.colorIndex = 0

        if self.bttnIndex > len(self.colors)-1:
            self.bttnIndex = 0

        self.config(bg=self.colors[self.colorIndex])

        self.colorBttn.config(bg = self.colors[self.bttnIndex])

    def lblChangeColor1(self, label):
        """ To use: self.lblChangeColor1()
         This is a function that will change the color of the labels as the number of clicks increases."""
        self.lblColorIndex += 1
        self.lblIndex = self.lblColorIndex+1

        if self.lblColorIndex > len(self.lblColors) - 1:
            self.lblColorIndex = 0

        if self.lblIndex > len(self.lblColors) - 1:
            self.lblIndex = 0

        label.config(bg=self.lblColors[self.lblColorIndex])

    def lblChangeColor2(self, label):
        """ To use: self.blChangeColor2()
                 This is a function that will change the color of the labels as the number of clicks decreases."""
        self.lblColorIndex -= 1
        self.lblIndex = self.lblColorIndex-1

        if (self.lblColorIndex > len(self.lblColors)) or (self.lblColorIndex < len(self.lblColors)):
            self.lblColorIndex = 0

        if (self.lblIndex > len(self.lblColors)) or (self.lblIndex < len(self.lblColors)):
            self.lblIndex = 0

        label.config(bg=self.lblColors[self.lblColorIndex])

    def calcSecs(self):
        """ To use: self.calcSecs()
                This is a function that will calculate how many seconds that the program has been open."""
        startTime = time.time()
        sec0 = time.time() - startTime

        sec = int(sec0)
        return sec

    def clicksPerSec(self):
        """ To use: self.clicksPerSec()
                This is a function that will calculate how many clicks have been done per second."""
        if self.secCalc == 0:
            self.secCalc += 0.01

            tapSec = self.clicks // (self.secCalc*100)

            if tapSec <= 0:
                tapSec = 0
        else:
            tapSec = (self.clicks // (self.secCalc*100))

            if tapSec <= 0:
                tapSec = 0

        tapSec = int(tapSec)
        self.tapPerSec = tapSec
        return self.tapPerSec

    def refreshClickLbl(self):
        clickTxt = self.tapPerSec

        self.lblClickPerSec.config(text=clickTxt)
        self.lblClickPerSec.after(1000, self.refreshClickLbl)


############# FIN #############

def main():
    ### Setting up GUI window ###
    root = Tk()  # Every Tkinter project needs this
    root.title("First GUI!")
    root.geometry("400x400")  # Setting the frame (window) height and width
    root.attributes("-fullscreen", False)
    ############ FIN ############

    app = App(root)

    root.mainloop()  # Calling up the window...

main()
## print("--- %s seconds ---" % (time.time() - start_time))