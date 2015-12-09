try:
    # for Python2 # using python 2 seems to cause read/write errors with our user file
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *

#mainGUI runs the "central nervous system" of the program.  Most user-side functions
#are called and offer exits back to the mainGUI.  It also houses the read/write commands
#that the other GUIs use to pull and write data to the text users file.
    
class mainGUI:
    def __init__(self, name, activeUser):
        self.name = name
        self.window = Tk() #create window
        self.window.title("Python Classroom ATM") #set window title
        #sets background size
        canvas = Canvas(self.window, width = 300, height = 150) 
        canvas.pack()

        #places buttons into window, links to definitions below
        userLabel = Label(self.window, text = "Logged in as:\n" + self.name).place(x = 20, y = 15)
        btDeposit = Button(self.window, text = "Deposit", command = self.deposit).place(x = 20, y = 60)
        btWithdraw = Button(self.window, text = "Withdraw", command = self.withdraw).place(x = 20, y = 100)
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
        userFile = open("users.txt", "r") #reads in user file
        #following statements search for current user and open that line
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
        userFile = open("users.txt", "r+") #opens file for writing
        #following statements search for current user to update information
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

#
# end of read/write methods, see top of section for details.
#######################################################################

    def checkBalance(self):
        #pulls information and calls the balanceGUI to display account information
        name = self.name
        activeUser = []
        activeUser = self.activeUser
        self.window.destroy()
        balanceGUI(name, activeUser)
        return
        
    def deposit(self):
        #pulls information and calls the depositGUI to process a deposit into account
        name = self.name
        activeUser = []
        activeUser = self.activeUser
        self.window.destroy()
        depositGUI(name, activeUser)
        return

    def withdraw(self):
        #pulls information and calls the withdrawGUI to process withdraw from account
        name = self.name
        activeUser = []
        activeUser = self.activeUser
        self.window.destroy()
        withdrawGUI(name, activeUser)
        return
      

    def transfer(self):
        #pulls information and calls the transferGUI to handle moving money between accounts
        name = self.name
        activeUser = []
        activeUser = self.activeUser
        self.window.destroy()
        transferGUI(name, activeUser)        
        return

    def logout(self):
        #closes program entirely
        self.window.destroy()
        return

#The depositGUI houses the options for depositing money into the accounts.  During its operation
#it will reference the transactionGUI to send the deposit information over for processing into the
#checking or savings accounts as the user desires.

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
        Entry(self.window, textvariable = self.depositAmount, justify = RIGHT).place(x = 105, y = 140) #entry window

        self.window.mainloop()

    def ten(self):
        #pulls information and relays a deposit of 10 to the transactionGUI
        name = self.name
        activeUser = self.activeUser
        amount = 10
        self.window.destroy()
        transactionGUI(name, activeUser, amount)
        return

    def twenty(self):
        #pulls information and relays a deposit of 20 to the transactionGUI
        name = self.name
        activeUser = self.activeUser
        amount = 20
        self.window.destroy()
        transactionGUI(name, activeUser, amount)
        return

    def fourty(self):
        #pulls information and relays a deposit of 40 to the transactionGUI
        name = self.name
        activeUser = self.activeUser
        amount = 40
        self.window.destroy()
        transactionGUI(name, activeUser, amount)
        return

    def fifty(self):
        #pulls information and relays a deposit of 50 to the transactionGUI
        name = self.name
        activeUser = self.activeUser
        amount = 50
        self.window.destroy()
        transactionGUI(name, activeUser, amount)
        return

    def seventy(self):
        #pulls information and relays a deposit of 60 to the transactionGUI
        name = self.name
        activeUser = self.activeUser
        amount = 75
        self.window.destroy()
        transactionGUI(name, activeUser, amount)
        return

    def hundred(self):
        #pulls information and relays a deposit of 100 to the transactionGUI
        name = self.name
        activeUser = self.activeUser
        amount = 100
        self.window.destroy()
        transactionGUI(name, activeUser, amount)
        return

    def enterPrice(self):
        #pulls information and relays a deposit of the user entered variable to the transactionGUI
        name = self.name
        activeUser = self.activeUser
        amount = float(self.depositAmount.get())#converts user variable into a float for processing
        self.window.destroy()
        transactionGUI(name, activeUser, amount)
        return


    def mainMenu(self):
        #Returns to and sends user information back to the main menu. 
        name = self.name
        activeUser = []
        activeUser = self.activeUser
        self.window.destroy()
        mainGUI(name, activeUser) 
        return

    
#The withdrawGUI houses the options for withdrawing money from the accounts.  During its operation
#it will reference the transactionGUI to send the withdraw information over for processing into the
#checking or savings accounts as the user desires.

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
        Entry(self.window, textvariable = self.withdrawAmount, justify = RIGHT).place(x = 105, y = 140) #entry window

        self.window.mainloop()


    def ten(self):
        #pulls information and relays a withdraw of 10 to the transactionGUI
        name = self.name
        activeUser = self.activeUser
        amount = -10
        self.window.destroy()
        transactionGUI(name, activeUser, amount)
        return

    def twenty(self):
        #pulls information and relays a withdraw of 20 to the transactionGUI
        name = self.name
        activeUser = self.activeUser
        amount = -20
        self.window.destroy()
        transactionGUI(name, activeUser, amount)
        return

    def fourty(self):
        #pulls information and relays a withdraw of 30 to the transactionGUI
        name = self.name
        activeUser = self.activeUser
        amount = -40
        self.window.destroy()
        transactionGUI(name, activeUser, amount)
        return

    def fifty(self):
        #pulls information and relays a withdraw of 40 to the transactionGUI
        name = self.name
        activeUser = self.activeUser
        amount = -50
        self.window.destroy()
        transactionGUI(name, activeUser, amount)
        return

    def seventy(self):
        #pulls information and relays a withdraw of 75 to the transactionGUI
        name = self.name
        activeUser = self.activeUser
        amount = -75
        self.window.destroy()
        transactionGUI(name, activeUser, amount)
        return

    def hundred(self):
        #pulls information and relays a withdraw of 100 to the transactionGUI 
        name = self.name
        activeUser = self.activeUser
        amount = -100
        self.window.destroy()
        transactionGUI(name, activeUser, amount)
        return

    def enterPrice(self):
        #pulls information and relays a withdraw of the user entered variable to the transactionGUI
        name = self.name
        activeUser = self.activeUser
        amount = -(float(self.withdrawAmount.get()))
        self.window.destroy()
        transactionGUI(name, activeUser, amount)
        return

    def mainMenu(self):
        #Returns to and sends user information back to the main menu.
        name = self.name
        activeUser = []
        activeUser = self.activeUser
        self.window.destroy()
        mainGUI(name, activeUser)
        return

#The transactionGUI is the work-horse of the program. This GUI receives the information
#from the deposit and withdraw GUIs and processes it accordingly.  Once the information
#is received, the GUI prompts the user whether they want the transaction to occur in the
#checking or savings accounts.

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


    def checking(self):
        #adjusts the balance of the checking account by the sent variable
        mainGUI.readUserFile(self)
        balanceCheck = float(self.activeUser[2]) + self.amount
        if balanceCheck >= 0:
            self.activeUser[2] = str(float(self.activeUser[2]) + self.amount)
            mainGUI.writeUserFile(self)
        else:
            name = self.name
            activeUser = []
            activeUser = self.activeUser
            self.window.destroy()
            noFunds(name, activeUser)
        return

    def savings(self):
        #adjusts the balance of the savings account by the sent variable
        mainGUI.readUserFile(self)
        balanceCheck = float(self.activeUser[3]) + self.amount
        if balanceCheck >= 0:
            self.activeUser[3] = str(float(self.activeUser[3]) + self.amount)
            mainGUI.writeUserFile(self)
        else:
            name = self.name
            activeUser = []
            activeUser = self.activeUser
            self.window.destroy()
            noFunds(name, activeUser)
        return

    def mainMenu(self):
        #Returns to and sends user information back to the main menu.
        name = self.name
        activeUser = []
        activeUser = self.activeUser
        self.window.destroy()
        mainGUI(name, activeUser)
        return

#The transferGUI is an option to allow users to move their money inbetween accounts. Users
#will enter the amount they wish to move, and then chose whether it moves from checking to
#savings, or savings to checking.  
    
class transferGUI():
    def __init__(self, name, activeUser):
        self.name = name
        self.activeUser = []
        self.activeUser = activeUser
        self.window = Tk() #create window
        self.window.title("Python Classroom ATM") #set window title
        #sets background size
        canvas = Canvas(self.window, width = 300, height = 150) 
        canvas.pack()        

        #places buttons into window, links to definitions below
        self.amount = StringVar()
        Label(self.window, text = "Enter Amount:").place(x = 20, y = 30) #Label for Entry box
        Entry(self.window, textvariable = self.amount, justify = RIGHT).place(x = 130, y = 30)
        btfromChecking = Button (self.window, text = "Checking to Savings", command = self.fromChecking).place(x = 20, y = 60)
        btfromChecking = Button (self.window, text = "Savings to Checking", command = self.fromSavings).place(x = 150, y = 60)
        btMainMenu = Button(self.window, text = "Return to Main menu", command = self.mainMenu).place(x = 80, y = 100)

        self.window.mainloop()

    def fromChecking(self):
        #transfers amount from checking to savings
        mainGUI.readUserFile(self) #reads file from mainGUI
        balanceCheck = float(self.activeUser[2]) - float(self.amount.get())
        if balanceCheck >= 0:
            self.activeUser[2] = str(float(self.activeUser[2]) -(float(self.amount.get()))) #sets new amount of checking less entered value
            self.activeUser[3] = str(float(self.activeUser[3]) +(float(self.amount.get()))) #sets new amount of savings less entered value
            mainGUI.writeUserFile(self) #writes the new values to file
        else:
            name = self.name
            activeUser = []
            activeUser = self.activeUser
            self.window.destroy()
            noFunds(name, activeUser)
        return
    
    def fromSavings(self):
        #transfers amount from savings to checking
        mainGUI.readUserFile(self) #reads file from mainGUI
        balanceCheck = float(self.activeUser[3]) - float(self.amount.get())
        if balanceCheck >= 0:
            self.activeUser[3] = str(float(self.activeUser[3]) -(float(self.amount.get()))) #sets new amount of checking less entered value
            self.activeUser[2] = str(float(self.activeUser[2]) +(float(self.amount.get()))) #sets new amount of savings less entered value
            mainGUI.writeUserFile(self) #writes the new values to file
        else:
            name = self.name
            activeUser = []
            activeUser = self.activeUser
            self.window.destroy()
            noFunds(name, activeUser)
        return

    def mainMenu(self):
        #Returns to and sends user information back to the main menu.
        name = self.name
        activeUser = []
        activeUser = self.activeUser
        self.window.destroy()
        mainGUI(name, activeUser)
        return

#The balanceGUI is the location the user can go to view their account information.  This
#GUI will return the user name, and their respective checking and savings balances

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
        Label(self.window, text = self.name).grid(row = 1, column = 2, sticky = E) #information pulled from data sent from mainGUI when called
        Label(self.window, text = self.balanceChecking()).grid(row = 2, column = 2, sticky = E) #calls information from balanceChecking
        Label(self.window, text = self.balanceSavings()).grid(row = 3, column = 2, sticky = E) #calls information from balanceSavings

        self.window.mainloop()


    def mainMenu(self):
        #Returns to and sends user information back to the main menu.
        name = self.name
        activeUser = []
        activeUser = self.activeUser
        self.window.destroy()
        mainGUI(name, activeUser) 
        return

    def balanceChecking(self):
        #pulls information about the current checking account
        name = self.name
        activeUser = []
        activeUser = self.activeUser
        #calls the mainGUI function to read the user file
        mainGUI.readUserFile(self)
        #sets balance equal to the checking list number
        balance = float(self.activeUser[2])
        returnBalance = "$" + "{0:.2f}".format(balance) #formats balance for currency display
        return (returnBalance) #returns balance for display

    def balanceSavings(self):
        #pulls information about the current savings account
        name = self.name
        activeUser = []
        activeUser = self.activeUser
        #calls the mainGUI function to read user file
        mainGUI.readUserFile(self)
        #sets balance equal to the savings list number
        balance = float(self.activeUser[3])
        returnBalance = "$" +  "{0:.2f}".format(balance) #formats balance for currency display
        return (returnBalance) #returns balance for display


#The noFundsGUI is a pop up window when the user attempts to withdraw
#or transfer more money out of an account than it has in it.
class noFunds():
    def __init__(self, name, activeUser):
        self.name = name
        self.activeUser = []
        self.activeUser = activeUser
        self.window = Tk() #create window
        self.window.title("Python Classroom ATM") #set window title

        #places labels into window to alert user why transaction failed.
        Label(self.window, text = "Transaction Failed:").grid(row = 1, column = 1, sticky = W)
        Label(self.window, text = "Reason: Insufficient Funds").grid(row = 2, column = 1, sticky = W)
        btMainMenu = Button(self.window, text = "Return to Main menu", command = self.mainMenu).grid(row = 3, column = 2, sticky = W)

        self.window.mainloop()

    def mainMenu(self):
        #Returns to and sends user information back to the main menu.
        name = self.name
        activeUser = []
        activeUser = self.activeUser
        self.window.destroy()
        mainGUI(name, activeUser) 
        return

            
    


