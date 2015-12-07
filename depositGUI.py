try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *

from transactionGUI import *

class depositGUI():
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
        btTen = Button(window, text = "Deposit $10", command = self.ten).place(x = 20, y = 20)
        btTwenty = Button(window, text = "Deposit $20", command = self.twenty).place(x = 20, y = 60)
        btFourty = Button(window, text = "Deposit $40", command = self.fourty).place(x = 20, y = 100)
        btFifty = Button(window, text = "Deposit $50", command = self.fifty).place(x = 200, y = 20)
        btSeventy = Button(window, text = "Deposit $75", command = self.seventy).place(x = 200, y = 60)
        btHundred = Button(window, text = "Deposit $100", command = self.hundred).place(x = 200, y = 100)
        btSubmit = Button(window, text = "Submit", command = self.enterPrice).place(x = 240, y = 140)
        btMainMenu = Button(window, text = "Return to Main menu", command = self.mainMenu).place(x = 100, y = 175)
        #begin creation of entry box for variable withdraw amount
        Label(window, text = "Enter Amount:").place(x = 20, y = 140) #Label for Entry box
        self.depositAmount = StringVar() #define variable for entry
        Entry(window, textvariable = self.depositAmount, justify = RIGHT).place(x = 110, y = 140) #entry window

        window.mainloop()

    def ten(self):
        #deposits 10
        name = self.name
        activeUser = self.activeUser
        amount = 10
        transactionGUI(name, activeUser, amount)
        return

    def twenty(self):
        #deposits 20
        name = self.name
        activeUser = self.activeUser
        amount = 20
        transactionGUI(name, activeUser, amount)
        return

    def fourty(self):
        #deposits 40 
        name = self.name
        activeUser = self.activeUser
        amount = 40
        transactionGUI(name, activeUser, amount)
        return

    def fifty(self):
        #deposits 50
        name = self.name
        activeUser = self.activeUser
        amount = 50
        transactionGUI(name, activeUser, amount)
        return

    def seventy(self):
        #deposits 75 
        name = self.name
        activeUser = self.activeUser
        amount = 75
        transactionGUI(name, activeUser, amount)
        return

    def hundred(self):
        #deposits 100 
        name = self.name
        activeUser = self.activeUser
        amount = 100
        transactionGUI(name, activeUser, amount)
        return

    def enterPrice(self):
        #deposits variable self.depositAmount
        name = self.name
        activeUser = self.activeUser
        amount = float(self.depositAmount.get())
        transactionGUI(name, activeUser, amount)
        return


    def mainMenu(self):
        #returns to mainGUI
        return

