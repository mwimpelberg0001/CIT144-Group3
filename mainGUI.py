try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *

class mainGUI:
    def __init__(self, name, activeUser):
        self.name = name
        self.window = Tk() #create window
        self.window.title("Python Classroom ATM") #set window title
        #sets background size
        canvas = Canvas(self.window, width = 300, height = 150) 
        canvas.pack()

        #places buttons into window, links to definitions below
        btDeposit = Button(self.window, text = "Deposit", command = self.deposit).place(x = 20, y = 20)
        btWithdraw = Button(self.window, text = "Withdraw", command = self.withdraw).place(x = 20, y = 60)
        btCheckBalance = Button(self.window, text = "Check Balance", command = self.checkBalance).place(x = 200, y = 20)
        btTransfer = Button(self.window, text = "Transfer Funds", command = self.transfer).place(x = 200, y = 60)
        btLogout = Button(self.window, text = "Log Out", command = self.logout).place(x = 200, y = 100)
        
        #reads in the user data of the logged in user
        self.activeUser = []
        self.activeUser = activeUser

        self.window.mainloop()

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
        name = self.name
        activeUser = []
        activeUser = self.activeUser
        self.window.destroy()
        balanceGUI(name, activeUser)
        return

#
# end of read/write methods, see top of section for details.
#######################################################################
        
    def deposit(self):
        name = self.name
        activeUser = []
        activeUser = self.activeUser
        self.window.destroy()
        depositGUI(name, activeUser)
        return

    def withdraw(self):
        name = self.name
        activeUser = []
        activeUser = self.activeUser
        self.window.destroy()
        withdrawGUI(name, activeUser)
        return
      

    def transfer(self):
        name = self.name
        activeUser = []
        activeUser = self.activeUser
        self.window.destroy()
        transferGUI(name, activeUser)        
        return

    def logout(self):
        #closes program
        self.window.destroy()
        return


class depositGUI():
    def __init__(self, name, activeUser):
        self.name = name
        self.activeUser = []
        self.activeUser = activeUser
        self.window = Tk() #create window
        self.window.title("Python Classroom ATM") #set window title
        #sets background size
        canvas = Canvas(self.window, width = 300, height = 200) 
        canvas.pack()

        #places buttons into window, links to definitions below
        btTen = Button(self.window, text = "Deposit $10", command = self.ten).place(x = 20, y = 20)
        btTwenty = Button(self.window, text = "Deposit $20", command = self.twenty).place(x = 20, y = 60)
        btFourty = Button(self.window, text = "Deposit $40", command = self.fourty).place(x = 20, y = 100)
        btFifty = Button(self.window, text = "Deposit $50", command = self.fifty).place(x = 200, y = 20)
        btSeventy = Button(self.window, text = "Deposit $75", command = self.seventy).place(x = 200, y = 60)
        btHundred = Button(self.window, text = "Deposit $100", command = self.hundred).place(x = 200, y = 100)
        btSubmit = Button(self.window, text = "Submit", command = self.enterPrice).place(x = 240, y = 140)
        btMainMenu = Button(self.window, text = "Return to Main menu", command = self.mainMenu).place(x = 100, y = 175)
        #begin creation of entry box for variable withdraw amount
        Label(self.window, text = "Enter Amount:").place(x = 20, y = 140) #Label for Entry box
        self.depositAmount = StringVar() #define variable for entry
        Entry(self.window, textvariable = self.depositAmount, justify = RIGHT).place(x = 110, y = 140) #entry window

        self.window.mainloop()

    def ten(self):
        #deposits 10
        name = self.name
        activeUser = self.activeUser
        amount = 10
        self.window.destroy()
        transactionGUI(name, activeUser, amount)
        return

    def twenty(self):
        #deposits 20
        name = self.name
        activeUser = self.activeUser
        amount = 20
        self.window.destroy()
        transactionGUI(name, activeUser, amount)
        return

    def fourty(self):
        #deposits 40 
        name = self.name
        activeUser = self.activeUser
        amount = 40
        self.window.destroy()
        transactionGUI(name, activeUser, amount)
        return

    def fifty(self):
        #deposits 50
        name = self.name
        activeUser = self.activeUser
        amount = 50
        self.window.destroy()
        transactionGUI(name, activeUser, amount)
        return

    def seventy(self):
        #deposits 75 
        name = self.name
        activeUser = self.activeUser
        amount = 75
        self.window.destroy()
        transactionGUI(name, activeUser, amount)
        return

    def hundred(self):
        #deposits 100 
        name = self.name
        activeUser = self.activeUser
        amount = 100
        self.window.destroy()
        transactionGUI(name, activeUser, amount)
        return

    def enterPrice(self):
        #deposits variable self.depositAmount
        name = self.name
        activeUser = self.activeUser
        amount = float(self.depositAmount.get())
        self.window.destroy()
        transactionGUI(name, activeUser, amount)
        return


    def mainMenu(self):
        name = self.name
        activeUser = []
        activeUser = self.activeUser
        self.window.destroy()
        mainGUI(name, activeUser) 
        #returns to mainGUI
        return

class withdrawGUI():
    def __init__(self, name, activeUser):
        self.name = name
        self.activeUser = []
        self.activeUser = activeUser
        self.window = Tk() #create window
        self.window.title("Python Classroom ATM") #set window title
        #sets background size
        canvas = Canvas(self.window, width = 300, height = 200) 
        canvas.pack()

        #places buttons into window, links to definitions below
        btTen = Button(self.window, text = "Withdraw $10", command = self.ten).place(x = 20, y = 20)
        btTwenty = Button(self.window, text = "Withdraw $20", command = self.twenty).place(x = 20, y = 60)
        btFourty = Button(self.window, text = "Withdraw $40", command = self.fourty).place(x = 20, y = 100)
        btFifty = Button(self.window, text = "Withdraw $50", command = self.fifty).place(x = 200, y = 20)
        btSeventy = Button(self.window, text = "Withdraw $75", command = self.seventy).place(x = 200, y = 60)
        btHundred = Button(self.window, text = "Withdraw $100", command = self.hundred).place(x = 200, y = 100)
        btSubmit = Button(self.window, text = "Submit", command = self.enterPrice).place(x = 240, y = 140)
        btMainMenu = Button(self.window, text = "Return to Main menu", command = self.mainMenu).place(x = 100, y = 175)
        #begin creation of entry box for variable withdraw amount
        Label(self.window, text = "Enter Amount:").place(x = 20, y = 140) #Label for Entry box
        self.withdrawAmount = StringVar() #define variable for entry
        Entry(self.window, textvariable = self.withdrawAmount, justify = RIGHT).place(x = 110, y = 140) #entry window

        self.window.mainloop()


    def ten(self):
        #withdraws 10
        name = self.name
        activeUser = self.activeUser
        amount = -10
        self.window.destroy()
        transactionGUI(name, activeUser, amount)
        return

    def twenty(self):
        #withdraws 20
        name = self.name
        activeUser = self.activeUser
        amount = -20
        self.window.destroy()
        transactionGUI(name, activeUser, amount)
        return

    def fourty(self):
        #withdraws 40 
        name = self.name
        activeUser = self.activeUser
        amount = -40
        self.window.destroy()
        transactionGUI(name, activeUser, amount)
        return

    def fifty(self):
        #withdraws 50
        name = self.name
        activeUser = self.activeUser
        amount = -50
        self.window.destroy()
        transactionGUI(name, activeUser, amount)
        return

    def seventy(self):
        #withdraws 75 
        name = self.name
        activeUser = self.activeUser
        amount = -75
        self.window.destroy()
        transactionGUI(name, activeUser, amount)
        return

    def hundred(self):
        #withdraws 100 
        name = self.name
        activeUser = self.activeUser
        amount = -100
        self.window.destroy()
        transactionGUI(name, activeUser, amount)
        return

    def enterPrice(self):
        #withdraws variable self.depositAmount
        name = self.name
        activeUser = self.activeUser
        amount = -(float(self.withdrawAmount.get()))
        self.window.destroy()
        transactionGUI(name, activeUser, amount)
        return


    def mainMenu(self):
        #returns to mainGUI
        name = self.name
        activeUser = []
        activeUser = self.activeUser
        self.window.destroy()
        mainGUI(name, activeUser)
        return

class transactionGUI():
    def __init__(self, name, activeUser, amount):
        self.name = name
        self.activeUser = []
        self.activeUser = activeUser
        self.amount = amount
        self.window = Tk() #create window
        self.window.title("Python Classroom ATM") #set window title
        #sets background size
        canvas = Canvas(self.window, width = 300, height = 150) 
        canvas.pack()

        #places buttons into window, links to definitions below
        btChecking = Button(self.window, text = "Checking", command = self.checking).place(x = 20, y = 20)
        btSavings = Button(self.window, text = "Savings", command = self.savings).place(x = 20, y = 60)
        btMainMenu = Button(self.window, text = "Return to Main menu", command = self.mainMenu).place(x = 100, y = 125)

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
        name = self.name
        activeUser = []
        activeUser = self.activeUser
        self.window.destroy()
        mainGUI(name, activeUser)
        return

class transferGUI():
    def __init__(self, name, activeUser):
        self.name = name
        self.activeUser = []
        self.activeUser = activeUser
        window = Tk() #create window
        window.title("Python Classroom ATM") #set window title
        #sets background size
        canvas = Canvas(window, width = 300, height = 200) 
        canvas.pack()        

        #places buttons into window, links to definitions below
        self.amount = StringVar()
        Entry(window, textvariable = self.amount, justify = RIGHT).place(x = 20, y = 20)
        btfromChecking = Button (window, text = "Checking to Savings", command = self.fromChecking).place(x = 20, y = 60)
        btfromChecking = Button (window, text = "Savings to Checking", command = self.fromSavings).place(x = 20, y = 100)

        window.mainloop()

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

    def fromChecking(self):
        #transfers amount from checking to savings
        self.readUserFile()
        self.activeUser[2] = str(float(self.activeUser[2]) -(float(self.amount.get())))
        self.activeUser[3] = str(float(self.activeUser[3]) +(float(self.amount.get())))
        self.writeUserFile()
        self.checkBalance()
        return
    
    def fromSavings(self):
        #transfers amount from savings to checking
        self.readUserFile()
        self.activeUser[3] = str(float(self.activeUser[3]) -(float(self.amount.get())))
        self.activeUser[2] = str(float(self.activeUser[2]) +(float(self.amount.get())))
        self.writeUserFile()
        self.checkBalance()
        return


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
        Label(self.window, textvariable = self.name).grid(row = 1, column = 2, sticky = E)
        Label(self.window, textvariable = self.balanceChecking).grid(row = 2, column = 2, sticky = E)
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
    

    


