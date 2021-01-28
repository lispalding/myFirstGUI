# MADE BY: Lisette Spalding
# FILE NAME: main.py
# DATE CREATED: 01/26/2021
# DATE LAST MODIFIED: 01/28/2021

############ IMPORTS ############
from tkinter import *
from tkinter import font as font
############## FIN ##############

######### GUI EDITING #########
class Pizza(Frame):
    """ To use: Pizza(root)
     This is the 'Pizza' class. It is creating the pizza order app. """
    def __init__(self, master):
        super(Pizza, self).__init__(master)
        self.grid()
        self.create()

    def create(self):
        """ To use: create()
         This is the 'create' class. It will create everything that is shown on the app."""
        ##### !! SETTING EVERYTHING UP ####
        ## LABELS ##
        self.lblCustomerNme = Label(self, text="Customer Name: ")
        self.lblAddr = Label(self, text="Address: ")
        self.lblPhoneNum = Label(self, text="Phone Number: ")
        self.lblSize = Label(self, text="Pizza Size: ")
        self.lblCrust = Label(self, text="Pizza Crust: ")
        self.lblToppings = Label(self, text="Pizza Toppings: ")
        #### FIN ####

        ## ENTRY ##
        self.customerNme = Entry(self, width=20)
        self.addr = Entry(self, width=20)
        self.phoneNum = Entry(self, width=20)
        ##### FIN ######

        ## CHECK BUTTON ##

        ####### FIN ######

        ## BUTTON ##
        self.submit = Button(self, text="Submit", command = self.test)
        #### FIN ####

        ### TEXT ###
        self.orderOut = Text(self)
        #### FIN ####
        #### FIN SETUP ####

        ## RADIO BUTTON ##
        # Size Button
        self.size = StringVar()
        self.size.set(None)
        Radiobutton(self,
                    variable=self.size,
                    text="Small",
                    value="small",
                    command = self.test
                    ).grid(row=4, column=0, sticky=W)
        Radiobutton(self,
                    variable=self.size,
                    text="Medium",
                    value="medium",
                    command = self.test
                    ).grid(row=4, column=0)
        Radiobutton(self,
                    variable=self.size,
                    text="Large",
                    value="large",
                    command = self.test
                    ).grid(row=4, column=0, sticky=E)
        self.size.set("large")

        # Crust Button
        self.crust = StringVar()
        self.crust.set(None)
        Radiobutton(self,
                    variable = self.size,
                    text="Normal",
                    value="normal"
                    ).grid(row=8, column=0, sticky=W)
        Radiobutton(self,
                    variable=self.size,
                    text="Stuffed",
                    value="stuffed"
                    ).grid(row=8, column=0)
        Radiobutton(self,
                    variable=self.size,
                    text="Thin",
                    value="thin"
                    ).grid(row=8, column=0, sticky=E)
        Radiobutton(self,
                    variable=self.size,
                    text="Pan",
                    value="pan"
                    ).grid(row=9, column=0, sticky=W)
        Radiobutton(self,
                    variable=self.size,
                    text="Deep Dish",
                    value="deep"
                    ).grid(row=9, column=0)
        Radiobutton(self,
                    variable=self.size,
                    text="Square",
                    value="square"
                    ).grid(row=9, column=0, sticky=E)

        ####### FIN #######

        #### CHECK BOXES ####
        self.pepperoni = BooleanVar()
        self.createCheckBox(self.pepperoni, "Pepperoni", 11, 0, W)

        self.mushrooms = BooleanVar()
        self.createCheckBox(self.mushrooms, "Mushrooms", 11, 0, EW)

        self.bacon = BooleanVar()
        self.createCheckBox(self.bacon, "Bacon", 11, 0, E)
        ######## FIN ########

        #### GRID PLACEMENT ####
        # Labels
        self.lblCustomerNme.grid(row=0, column=0, sticky=W)
        self.lblAddr.grid(row=1, column=0, sticky=W)
        self.lblPhoneNum.grid(row=2, column=0, sticky=W)
        self.lblSize.grid(row=3, column=0, sticky=W)
        self.lblCrust.grid(row=6, column=0, sticky=W)
        self.lblToppings.grid(row=10, column=0, sticky=W)

        # Entry(s)
        self.customerNme.grid(row=0, column=0, sticky=E)
        self.addr.grid(row=1, column=0, sticky=E)
        self.phoneNum.grid(row=2, column=0, sticky=E)

        # Buttons
        self.submit.grid(row=17, column=0)

        # Text
        self.orderOut.grid(row=18, column=0)
        #### FIN PLACEMENT ####

        #### CONFIGURATIONS ####
        self.orderOut.config(width=35)
        #### CONFIGURATION FIN ###

    def createCheckBox(self, var, top, r, c, st):
        Checkbutton(self,
                    variable=var,
                    text=top
                    ).grid(row=r, column=c, sticky=st)

    def test(self):
        orderSize = self.size.get()
        orderCrust = self.crust.get()
        toppings = []
        x = ""
        for i in range(len(toppings)):
            x+= toppings[i]
        if self.pepperoni.get():
            toppings.append("Pepperoni")
        if self.mushrooms.get():
            toppings.append("Mushrooms")
        if self.bacon.get():
            toppings.append("Bacon")

        order = orderSize + orderCrust + x
        self.orderOut.delete(0.0, END)
        self.orderOut.insert(0.0, order)
############# FIN #############

###### Setting up GUI window ######
root = Tk() # Every Tkinter project needs this
root.title("Pizza Order!")
root.geometry("300x450") # Setting the frame (window) height and width
root.attributes("-fullscreen", False)
############### FIN ###############

pizza = Pizza(root)

root.mainloop()