try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *

from withdrawGUI import *
from depositGUI import *

class mainGUI:
    def __init__(self, name, activeUser):
        self.name = name
        window = Tk() #create window
        window.title("Python Classroom ATM") #set window title
        #sets background size
        canvas = Canvas(window, width = 300, height = 150) 
        canvas.pack()

        #places buttons into window, links to definitions below
        btDeposit = Button(window, text = "Deposit", command = self.deposit).place(x = 20, y = 20)
        btWithdraw = Button(window, text = "Withdraw", command = self.withdraw).place(x = 20, y = 60)
        btQuickWithdraw = Button(window, text = "Quick Withdraw $40", command = self.quickWithdraw).place(x = 20, y = 100)
        btCheckBalance = Button(window, text = "Check Balance", command = self.checkBalance).place(x = 200, y = 20)
        btTransfer = Button(window, text = "Transfer Funds", command = self.transfer).place(x = 200, y = 60)
        btLogout = Button(window, text = "Log Out", command = self.logout).place(x = 200, y = 100)
        
        #reads in the user data of the logged in user
        self.activeUser = []
        self.activeUser = activeUser

        window.mainloop()
        
#################################################
# userFile read and write methods, any method needing to read/write 
# the user file should be made to call these functions using "mainGUI.readUserFile()"
# or "mainGUI.writeUserFile()" (for all programs, deposit, withdraw, transfer etc..)
#
    def readUserFile(self):
        if self.name == 'user':
            userFile = open('users/user.txt', 'r')
        elif self.name == 'mwimpelberg':
            userFile = open('users/mwimpelberg.txt', 'r')
        elif self.name == 'jwood':
            userFile = open('users/jwood.txt', 'r')
        elif self.name == 'dkrebs':
            userFile = open('users/dkrebs.txt', 'r')
        self.activeUser = str(userFile.readline()).split(',')
        userFile.close()
        return
    
    def writeUserFile(self):
        if self.name == 'user':
            userFile = open('users/user.txt', 'r+')
        elif self.name == 'mwimpelberg':
            userFile = open('users/mwimpelberg.txt', 'r+')
        elif self.name == 'jwood':
            userFile = open('users/jwood.txt', 'r+')
        elif self.name == 'dkrebs':
            userFile = open('users/dkrebs.txt', 'r+')
        for x in range(0,4):
            userFile.write(str(self.activeUser[x]) + ',')
        userFile.close()
        return

    def checkBalance(self):
        self.readUserFile()
        #for item in self.activeUser:
          #  print (str(item))
        checking = self.activeUser[2]
        savings = self.activeUser[3] 
        print (str( "checking: $" + checking + "\tsavings: $" + savings ))
        return checking, savings

#
# end of read/write methods, see top of section for details.
#######################################################################
        
    def deposit(self):
        name = self.name
        activeUser = []
        activeUser = self.activeUser
        depositGUI(name, activeUser)
        return

    def withdraw(self):
        name = self.name
        activeUser = []
        activeUser = self.activeUser
        withdrawGUI(name, activeUser)
        return
      
    def quickWithdraw(self):
        #automatically withdraws 40 from balance
        self.readUserFile()
        self.activeUser[2] = str(float(self.activeUser[2]) - 40)
        self.writeUserFile()
        self.checkBalance()
        return

    def transfer(self):
        import transferGUI
        return

    def logout(self):
        #closes program
        window.destroy()
        return
