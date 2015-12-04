try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *

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


    def pullUserFile(self):
    	userFile = open("users.txt", "r")
    	self.validID = str(userFile.readline())
    	self.validPass = str(userFile.readline())
    	self.userBalance = float(userFile.readline())
    	userFile.close()
    	return
    
    def deposit(self):
        import depositGUI
        return

    def withdraw(self):
        import withdrawGUI
        return

    def quickWithdraw(self):
        #automatically withdraws 40 from balance
        userFile = open("users.txt", "r+")
    	user = str(userFile.readline())
    	password = str(userFile.readline())
    	balance = float(userFile.readline())
    	if (balance - 40) >= 0.0:
    		balance -= 40
    	userFile.seek(0)
    	userFile.write(user)
    	userFile.write(password)
    	userFile.write(str(balance))
    	userFile.truncate()
    	userFile.close()
        return

    def checkBalance(self):
        userFile = open("users.txt", "r")
    	user = str(userFile.readline())
    	password = str(userFile.readline())
    	balance = float(userFile.readline())
        return balance

    def transfer(self):
        import transferGUI
        return

    def logout(self):
        #closes program
        return

#only purpose is to call mainGUI for viewing
mainGUI()

    

