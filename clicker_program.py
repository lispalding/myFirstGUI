# MADE BY: Lisette Spalding
# FILE NAME: clicker_program.py
# PYTHON VER. USED: 3.8
# DATE CREATED: 01/20/2021
# DATE LAST MODIFIED: 02/06/2021

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
        self.time0 = time.time()

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
        self.lblClickPerSec = Label(self, text=self.tapPerSec)

        ## Label Configuration
        self.after(1000, self.lblReset)

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
        self.addBttn["command"] = self.updateAndAdd
        self.minBttn["command"] = self.updateAndSubtract
        self.colorBttn["command"] = self.changeColor

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

        self.calcSecs()


    def subtractFromCount(self):
        """ To use: self.subtractFromAccount()
         This is a method that subtracts from the click count."""
        self.calcSecs()

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
        time1 = time.time()

        timeSec = self.time0 - time1

        sec = timeSec*-1
        sec = int(sec)
        return sec

    def clicksPerSec(self):
        """ To use: self.clicksPerSec()
                This is a function that will calculate how many clicks have been done per second."""
        if self.secCalc == 0:
            tapSec = 0
        else:
            tapSec = (self.clicks // self.secCalc)

        tapSec = int(tapSec)
        self.tapPerSec = str(tapSec)
        return self.tapPerSec

    def refreshSec(self):
        self.secCalc = self.calcSecs()

        self.after(1000, self.refreshSec)
        return self.secCalc

    def lblReset(self):
        self.lblClickPerSec["text"] = " "
        self.lblClickPerSec["text"] = "0"

        self.after(1000, self.lblReset)

    def updateAndAdd(self):
        self.addToCount()
        self.clickTxt = self.clicksPerSec()

        self.lblClickPerSec["text"] = " "
        self.lblClickPerSec["text"] = self.clickTxt
        return self.lblClickPerSec

    def updateAndSubtract(self):
        self.subtractFromCount()
        self.clickTxt = self.clicksPerSec()

        self.lblClickPerSec["text"] = " "
        self.lblClickPerSec["text"] = self.clickTxt
        return self.lblClickPerSec


############# FIN #############

def main():
    ### Setting up GUI window ###
    root = Tk()  # Every Tkinter project needs this
    root.title("Clicker Program!")
    root.geometry("400x400")  # Setting the frame (window) height and width
    root.attributes("-fullscreen", False)
    ############ FIN ############

    app = App(root)

    app.refreshSec()
    root.mainloop()  # Calling up the window...

main()
## print("--- %s seconds ---" % (time.time() - start_time))