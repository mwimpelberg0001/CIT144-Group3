from tkinter import *

class mainGUI():
    def __init__(self):
        window = Tk() #create window
        window.title("Python Classroom ATM") #set window title
        canvas = Canvas(window, width = 300, height = 150)
        canvas.pack()

        btDeposit = Button(window, text = "Deposit", command = self.deposit).place(x = 20, y = 20)
        btWithdraw = Button(window, text = "Withdraw", command = self.withdraw).place(x = 20, y = 60)
        btQuickWithdraw = Button(window, text = "Quick Withdraw $40", command = self.quickWithdraw).place(x = 20, y = 100)
        btCheckBalance = Button(window, text = "Check Balance", command = self.checkBalance).place(x = 200, y = 20)
        btTransfer = Button(window, text = "Transfer Funds", command = self.transfer).place(x = 200, y = 60)
        btLogout = Button(window, text = "Log Out", command = self.logout).place(x = 200, y = 100)

#        label1.grid(row = 1, column = 1)
#        btDeposit.grid(row = 2, column = 1)
#        btWithdraw.grid(row = 3, column = 1)
#        btQuickWithdraw.grid(row = 4, column = 1)
#        btCheckBalance.grid(row = 2, column = 2)
#        btTransfer.grid(row = 3, column = 2)
#        btLogout.grid(row = 5, column = 2)


    def deposit(self):
        return

    def withdraw(self):
        return

    def quickWithdraw(self):
        return

    def checkBalance(self):
        return

    def transfer(self):
        return

    def logout(self):
        return

mainGUI()

    

