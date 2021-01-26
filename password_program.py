# MADE BY: Lisette Spalding
# FILE NAME: main.py
# DATE CREATED: 01/26/2021
# DATE LAST MODIFIED: 01/26/2021

############ IMPORTS ############
from tkinter import *
from tkinter import font as font
############## FIN ##############

######### GUI EDITING #########
class Password(Frame):
    """ To use: Password(root)
    This is the Password class, it will build a password window. """
    usernames = ["Lisette"]
    passwords = ["Password"]

    def __init__(self, master):
        super(Password, self).__init__(master)
        self.grid()
        self.create()
        self.tries = 0

    def create(self):
        """ To use: create()
         This is the create function. It will create the widgets."""
        ## LABLES ##
        self.lblMain = Label(self, text="Welcome! Please enter the required information.")
        self.lblUser = Label(self, text="Enter Username: ")
        self.lblPass = Label(self, text="Enter Password: ")
        #### FIN ####

        ## BUTTONS ##
        self.submitBttn = Button(self, text="Submit!")
        #### FIN ####

        ### ENTRY ###
        self.userEnt = Entry(self, width=40)
        self.passEnt = Entry(self, width=40)
        #### FIN ####

        ### TEXT ###
        self.output = Text(self)
        #### FIN ####

        ## Placing everything on the grid
        # Labels
        self.lblMain.grid(row=0, column=0, columnspan=3)
        self.lblUser.grid(row=1, column=0, sticky=NW)
        self.lblPass.grid(row=2, column=0, sticky=SW)

        # Entry(s)
        self.userEnt.grid(row=1, column=1, columnspan=2, sticky=W)
        self.passEnt.grid(row=2, column=1, columnspan=2, sticky=W)

        # Button(s)
        self.submitBttn.grid(row=3, column=0, sticky=W)

        # Text Fields
        self.output.grid(row=4, column=0, columnspan=3)

        ## Commands
        self.submitBttn["command"]=self.submit

        ## Configurations
        # Entry(s)
        self.passEnt.config(show="*")

        # Text Entries
        self.output.config(width=40)

    def submit(self):
        """ To use: submit()
         This is a variable that operates when you click the submit button."""
        username = self.userEnt.get()
        password = self.passEnt.get()

        if username in self.usernames:
            if password in self.passwords:
                message = "You got in!"
            else:
                message = "Wrong password."
                self.tries += 1
        else:
            message = "Wrong username."
            self.tries +=1

        self.output.delete(0.0, END)
        self.output.insert(0.0, message)

        if self.tries > 3:
            message = "Messaging the Police, you're trying to access private information."
            self.output.delete(0.0, END)
            self.output.insert(0.0, message)

            self.userEnt.configure(state=DISABLED)
            self.passEnt.configure(state=DISABLED)
            self.submitBttn.configure(state=DISABLED)

        print(message)


############# FIN #############

###### Setting up GUI window ######
root = Tk() # Every Tkinter project needs this
root.title("Password!")
root.geometry("300x450") # Setting the frame (window) height and width
root.attributes("-fullscreen", False)
############### FIN ###############

psswrd = Password(root)

root.mainloop()