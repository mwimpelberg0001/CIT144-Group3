from tkinter import *

class depositGUI():
    def __init__(self):
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



    def ten(self):
        #removes 10 from balance
        return

    def twenty(self):
        #removes 20 from balance
        return

    def fourty(self):
        #removes 40 from balance
        return

    def fifty(self):
        #removes 50 from balance
        return

    def seventy(self):
        #removes 75 from balance
        return

    def hundred(self):
        #removes 100 from balance
        return

    def enterPrice(self):
        #removes variable self.depositAmount from balance
        #will need to check and convert StringVar to number
        #may need to check for invalid input could create a seperate
        #function for this as we will need to use it for withdraw.
        return

    def mainMenu(self):
        #returns to mainGUI
        return

#only purpose is to call mainGUI for viewing
depositGUI()

    

