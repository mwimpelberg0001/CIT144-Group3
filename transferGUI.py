try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *


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
        self.activeUser[2] = str(float(self.activeUser[2]) - self.amount)
        self.activeUser[3] = str(float(self.activeUser[3]) + self.amount)
        self.writeUserFile()
        self.checkBalance()
        return
    
    def fromSavings(self):
        #transfers amount from savings to checking
        self.readUserFile()
        self.activeUser[3] = str(float(self.activeUser[3]) - self.amount)
        self.activeUser[2] = str(float(self.activeUser[2]) + self.amount)
        self.writeUserFile()
        self.checkBalance()
        return
