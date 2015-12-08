#this will take input of account name and use that to pull
#checking and savings balances.  This function needs a lot
#of work to define functions to pull and get values then add
#them back into the GUI

from tkinter import *
from mainGUI import *

class balanceGUI():
    def __init__(self, name, activeUser):
        self.name = name
        self.activeUser = []
        self.activeUser = activeUser
        self.window = Tk() #create window
        self.window.title("Python Classroom ATM") #set window title

        #places labels into window
        Label(self.window, text = "Account Name:").grid(row = 1, column = 1, sticky = W)
        Label(self.window, text = "Checking Balance:").grid(row = 2, column = 1, sticky = W)
        Label(self.window, text = "Savings Balance:").grid(row = 3, column = 1, sticky = W)
        btMainMenu = Button(self.window, text = "Return to Main menu", command = self.mainMenu).grid(row = 4, column = 2, sticky = W)

        #puts the amounts to the right of labels in window
        self.accountName = StringVar()
        self.accountName.set("John Doe") #just added to show a value
        Label(self.window, textvariable = self.accountName).grid(row = 1, column = 2, sticky = E)

        self.balanceChecking = StringVar()
        self.balanceChecking.set(format(1137, "10.2f")) #just added to show a value
        Label(self.window, textvariable = self.balanceChecking).grid(row = 2, column = 2, sticky = E)

        self.balanceSavings = StringVar()
        self.balanceSavings.set(format(1234, "10.2f")) #just added to show a value
        Label(self.window, textvariable = self.balanceSavings).grid(row = 3, column = 2, sticky = E)

        self.window.mainloop()


    def mainMenu(self):
        #returns to mainGUI
        name = self.name
        activeUser = []
        activeUser = self.activeUser
        self.window.destroy()
        mainGUI(name, activeUser) 
        return
    

    

