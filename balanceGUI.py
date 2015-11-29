#this will take input of account name and use that to pull
#checking and savings balances.  This function needs a lot
#of work to define functions to pull and get values then add
#them back into the GUI

from tkinter import *

class balanceGUI():
    def __init__(self):
        window = Tk() #create window
        window.title("Python Classroom ATM") #set window title

        #places labels into window
        Label(window, text = "Account Name:").grid(row = 1, column = 1, sticky = W)
        Label(window, text = "Checking Balance:").grid(row = 2, column = 1, sticky = W)
        Label(window, text = "Savings Balance:").grid(row = 3, column = 1, sticky = W)
        btMainMenu = Button(window, text = "Return to Main menu", command = self.mainMenu).grid(row = 4, column = 2, sticky = W)

        #puts the amounts to the right of labels in window
        self.accountName = StringVar()
        self.accountName.set("John Doe") #just added to show a value
        Label(window, textvariable = self.accountName).grid(row = 1, column = 2, sticky = E)

        self.balanceChecking = StringVar()
        self.balanceChecking.set(format(1137, "10.2f")) #just added to show a value
        Label(window, textvariable = self.balanceChecking).grid(row = 2, column = 2, sticky = E)

        self.balanceSavings = StringVar()
        self.balanceSavings.set(format(1234, "10.2f")) #just added to show a value
        Label(window, textvariable = self.balanceSavings).grid(row = 3, column = 2, sticky = E)

        window.mainloop()


    def mainMenu(self):
        #returns to mainGUI
        return

#only purpose is to call mainGUI for viewing
balanceGUI()

    

