# MADE BY: Lisette Spalding
# FILE NAME: layout.py
# DATE CREATED: 02/01/2021
# DATE LAST MODIFIED: 02/01/2021

## !! ...THIS FILE IS LAYOUT PRACTICE... !! ##

############ IMPORTS ############
from PIL import Image, ImageTk
from tkinter import Tk, BOTH
from tkinter.ttk import Frame, Label, Style, Button
############## FIN ##############

Height = 300
Width = 280

############ CLASSES ############
class App(Frame):
    def __init__(self, master):
        super(App, self).__init__(master)
        # This will pack everything to the size that it needs to be automatically:
        self.pack(fill=BOTH,expand=1)
        self.create()

    def create(self):
        Label(text="Absolute Positioning").place(x=0,y=0)
        Label(text="Absolute Positioning...").place(x=0,y=17)

        # Button(text="Click Me").place(x=Width/2,y=Height/2)

        img1 = Image.open("rhea.jpg")
        firstImg = ImageTk.PhotoImage(img1)
        self.lbl1 = Label(self, image=firstImg)
        self.lbl1.image = firstImg
        self.lbl1.place(x=0,y=60)

        img2 = Image.open("apollo2.jpg")
        secondImg = ImageTk.PhotoImage(img2)
        self.lbl2 = Label(self, image=secondImg)
        self.lbl2.image = secondImg
        self.lbl2.place(x=250, y=60)

        img3 = Image.open("rose.jpg")
        thirdImg = ImageTk.PhotoImage(img3)
        self.lbl3 = Label(self, image=thirdImg)
        self.lbl3.image = thirdImg
        self.lbl3.place(x=530, y=60)

############## FIN ##############

def main():
    root = Tk()
    root.geometry("300x280+300+300")

    app = App(root)

    root.mainloop()

main()