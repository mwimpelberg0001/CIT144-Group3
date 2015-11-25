from tkinter import *

class mainGUI():
    def __init__(self,userID):
        self.__userID = userID
        window = Tk() #create window
        window.title("Please Selection from one of the following options") #set window title

        frame1 = Frame(window)
        frame1.pack()
        label1 = Label(frame1, text = "Please Selection from one of the following options")
        btDeposit = Button(frame1, text = "Deposit", command = self.deposit)
        btWithdraw = Button(frame1, text = "Withdraw", command = self.withdraw)
        btQuickWithdraw = Button(frame1, text = "Quick Withdraw $40", command = self.quickWithdraw)
        btCheckBalance = Button(frame1, text = "Check Balance", command = self.checkBalance)
        btTransfer = Button(frame1, text = "Transfer Funds", command = self.transfer)
        btLogout = Button(frame1, text = "Log Out", command = self.logout)

        label1.grid(row = 1, column = 1)
        btDeposit.grid(row = 2, column = 1)
        btWithdraw.grid(row = 3, column = 1)
        btQuickWithdraw.grid(row = 4, column = 1)
        btCheckBalance.grid(row = 2, column = 2)
        btTransfer.grid(row = 3, column = 2)
        btLogout.grid(row = 5, column = 2)


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

name = "Keith"
mainGUI(name)

    

