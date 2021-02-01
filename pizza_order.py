# MADE BY: Lisette Spalding
# FILE NAME: main.py
# DATE CREATED: 01/26/2021
# DATE LAST MODIFIED: 02/01/2021

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
        self.customerNme = Entry(self)
        self.addr = Entry(self)
        self.phoneNum = Entry(self)
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
                    ).grid(row=4, column=1, sticky=W)
        Radiobutton(self,
                    variable=self.size,
                    text="Large",
                    value="large",
                    command = self.test
                    ).grid(row=4, column=2, sticky=W)
        self.size.set("large")

        # Crust Button
        self.crust = StringVar()
        self.crust.set(None)
        Radiobutton(self,
                    variable = self.crust,
                    text="Normal",
                    value="normal"
                    ).grid(row=8, column=0, sticky=W)
        Radiobutton(self,
                    variable = self.crust,
                    text="Stuffed",
                    value="stuffed"
                    ).grid(row=8, column=1, sticky=W)
        Radiobutton(self,
                    variable = self.crust,
                    text="Thin",
                    value="thin"
                    ).grid(row=8, column=2, sticky=W)
        Radiobutton(self,
                    variable=self.crust,
                    text="Pan",
                    value="pan"
                    ).grid(row=9, column=0, sticky=W)
        Radiobutton(self,
                    variable = self.crust,
                    text="Deep Dish",
                    value="deep"
                    ).grid(row=9, column=1, sticky=W)
        Radiobutton(self,
                    variable = self.crust,
                    text="Square",
                    value="square"
                    ).grid(row=9, column=2, sticky=W)
        self.crust.set("deep")

        ####### FIN #######

        #### CHECK BOXES ####
        self.pepperoni = BooleanVar()
        self.createCheckBox(self.pepperoni, "Pepperoni", 11, 0)

        self.ham = BooleanVar()
        self.createCheckBox(self.ham, "Ham", 11, 1)

        self.bacon = BooleanVar()
        self.createCheckBox(self.bacon, "Bacon", 11, 2)

        self.chicken = BooleanVar()
        self.createCheckBox(self.chicken, "Chicken", 12, 0)

        self.sausage = BooleanVar()
        self.createCheckBox(self.sausage, "Sausage", 12, 1)

        self.beef = BooleanVar()
        self.createCheckBox(self.beef, "Beef", 12, 2)

        self.salami = BooleanVar()
        self.createCheckBox(self.salami, "Salami", 13, 0)

        self.prosciutto = BooleanVar()
        self.createCheckBox(self.prosciutto, "Prosciutto", 13, 1)

        self.meatball = BooleanVar()
        self.createCheckBox(self.meatball, "Meatballs", 13, 2)

        self.mushroom = BooleanVar()
        self.createCheckBox(self.mushroom, "Mushrooms", 14, 0)

        self.pineapple = BooleanVar()
        self.createCheckBox(self.pineapple, "Pineapple", 14, 1)

        self.onion = BooleanVar()
        self.createCheckBox(self.onion, "Onions", 14, 2)

        self.olive = BooleanVar()
        self.createCheckBox(self.olive, "Olives", 15, 0)

        self.bellPepper = BooleanVar()
        self.createCheckBox(self.bellPepper, "Bell Peppers", 15, 1)

        self.tomato = BooleanVar()
        self.createCheckBox(self.tomato, "Tomato", 15, 2)

        self.jalapeno = BooleanVar()
        self.createCheckBox(self.jalapeno, "Jalapeno", 16, 0)

        self.garlic = BooleanVar()
        self.createCheckBox(self.garlic, "Garlic", 16, 1)

        self.spinach = BooleanVar()
        self.createCheckBox(self.spinach, "Spinach", 16, 2)
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
        self.customerNme.grid(row=0, column=2)
        self.addr.grid(row=1, column=2)
        self.phoneNum.grid(row=2, column=2)

        # Buttons
        self.submit.grid(row=17, column=0)

        # Text
        self.orderOut.grid(row=18, column=0, columnspan=3)
        #### FIN PLACEMENT ####

        #### CONFIGURATIONS ####
        self.orderOut.config(width=35, height=16)
        #### CONFIGURATION FIN ###

    def createCheckBox(self, var, top, r, c):
        Checkbutton(self,
                    variable=var,
                    text=top
                    ).grid(row=r, column=c, sticky=W)

    def test(self):
        orderSize = self.size.get()
        orderCrust = self.crust.get()
        toppings = []
        x = ""
        for i in range(len(toppings)):
            x+= toppings[i]
        if self.pepperoni.get():
            toppings.append("Pepperoni")
        if self.ham.get():
            toppings.append("Ham")
        if self.bacon.get():
            toppings.append("Bacon")
        if self.chicken.get():
            toppings.append("Chicken")
        if self.sausage.get():
            toppings.append("Sausage")
        if self.prosciutto.get():
            toppings.append("Prosciutto")
        if self.meatball.get():
            toppings.append("Meatball")
        if self.mushroom.get():
            toppings.append("Mushroom")
        if self.pineapple.get():
            toppings.append("Pineapple")
        if self.onion.get():
            toppings.append("Onion")
        if self.olive.get():
            toppings.append("Olive")
        if self.bellPepper.get():
            toppings.append("Bell Pepper")
        if self.tomato.get():
            toppings.append("Tomato")
        if self.jalapeno.get():
            toppings.append("Jalapeno")
        if self.garlic.get():
            toppings.append("Garlic")
        if self.spinach.get():
            toppings.append("Spinach")

        order = orderSize + orderCrust + x
        for top in toppings:
            order += top

        self.orderOut.delete(0.0, END)
        self.orderOut.insert(0.0, order)
############# FIN #############

###### Setting up GUI window ######
root = Tk() # Every Tkinter project needs this
root.title("Pizza Order!")
root.geometry("330x650") # Setting the frame (window) height and width
root.attributes("-fullscreen", False)
############### FIN ###############

pizza = Pizza(root)

root.mainloop()