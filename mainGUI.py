from Tkinter import *

class mainGUI():
    def __init__(self):
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


    def deposit(self):
        #call deposit window menu
        return

    def withdraw(self):
        #to call withdraw window menu
        return

    def quickWithdraw(self):
        #automatically withdraws 40 from balance
        return

    def checkBalance(self):
        #returns balance amount
        return

    def transfer(self):
        #pulls transfer window
        return

    def logout(self):
        #closes program
        return

#only purpose is to call mainGUI for viewing
mainGUI()

    

