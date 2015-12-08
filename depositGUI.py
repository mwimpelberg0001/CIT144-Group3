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

