try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *

from transactionGUI import *

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
