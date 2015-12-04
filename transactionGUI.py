#this will take input of two variables and adjust balances of accounts
#based on input. Current condition is only designed for viewing GUI. Future
#transactions for deposit, withdraw, and quick withdraw will use this
#and pass the desired amounts for selection from/to checking and savings.

try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *


class quickGUI():
    def __init__(self):
        window = Tk() #create window
        window.title("Python Classroom ATM") #set window title
        #sets background size
        canvas = Canvas(window, width = 300, height = 150) 
        canvas.pack()

        #places buttons into window, links to definitions below
        btChecking = Button(window, text = "From Checking", command = self.checking).place(x = 20, y = 20)
        btSavings = Button(window, text = "From Savings", command = self.savings).place(x = 20, y = 60)
        btMainMenu = Button(window, text = "Return to Main menu", command = self.mainMenu).place(x = 100, y = 125)


    def checking(self):
        #removes X from balance
        return

    def savings(self):
        #removes X from balance
        return

    def mainMenu(self):
        #returns to mainGUI
        return

#only purpose is to call mainGUI for viewing
quickGUI()

    

