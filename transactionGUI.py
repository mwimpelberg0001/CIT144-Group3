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


class transactionGUI():
    def __init__(self, name, activeUser, amount):
        self.name = name
        self.activeUser = []
        self.activeUser = activeUser
        self.amount = amount
        window = Tk() #create window
        window.title("Python Classroom ATM") #set window title
        #sets background size
        canvas = Canvas(window, width = 300, height = 150) 
        canvas.pack()

        #places buttons into window, links to definitions below
        btChecking = Button(window, text = "Checking", command = self.checking).place(x = 20, y = 20)
        btSavings = Button(window, text = "Savings", command = self.savings).place(x = 20, y = 60)
        btMainMenu = Button(window, text = "Return to Main menu", command = self.mainMenu).place(x = 100, y = 125)

#################################################
# userFile read and write methods, any method needing to read/write 
# the user file should be made to call these functions using "mainGUI.readUserFile()"
# or "mainGUI.writeUserFile()" (for all programs, deposit, withdraw, transfer etc..)
#
    def readUserFile(self):
        userFile = open("users.txt", "r")
        if self.name == 'user':
            userFile.seek(0)
        elif self.name == 'mwimpelberg':
            userFile.seek(32)
        elif self.name == 'jwood':
            userFile.seek(64)
        elif self.name == 'dkrebs':
            userFile.seek(96)
        #print str(self.activeUser)
        self.activeUser = str(userFile.readline()).split(',')
        #print str(self.activeUser)
        userFile.close()
        return
    
    def writeUserFile(self):
        userFile = open("users.txt", "r+")
        if self.name == 'user':
            userFile.seek(0)
        elif self.name == 'mwimpelberg':
            userFile.seek(32)
        elif self.name == 'jwood':
            userFile.seek(64)
        elif self.name == 'dkrebs':
            userFile.seek(96)
        for x in range(0,4):
            userFile.write(str(self.activeUser[x]) + ',')
        userFile.close()
        return

    def checkBalance(self):
        self.readUserFile()
        checking = self.activeUser[2]
        savings = self.activeUser[3] 
        print (str( "checking: $" + checking + "\tsavings: $" + savings ))
        return checking, savings

#
# end of read/write methods, see top of section for details.
#######################################################################

    def checking(self):
        #adjusts X on balance
        self.readUserFile()
        self.activeUser[2] = str(float(self.activeUser[2]) + self.amount)
        self.writeUserFile()
        self.checkBalance()
        return

    def savings(self):
        #adjusts X on balance
        self.readUserFile()
        self.activeUser[3] = str(float(self.activeUser[3]) + self.amount)
        self.writeUserFile()
        self.checkBalance()
        return

    def mainMenu(self):
        #returns to mainGUI
        return
