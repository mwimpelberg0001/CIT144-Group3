try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *

class loginGUI:
    def __init__(self):
        window = Tk() #create window
        window.title("Python Classroom ATM") #set window title

        frame1 = Frame(window)
        frame1.pack()
        label1 = Label(frame1, text = "User ID: ") #Set label for first entry field
        self.userID = StringVar() #define variable to store userID
        entryID = Entry(frame1, textvariable = self.userID) #Enter userID
        label2 = Label(frame1, text = "Password: ") #Set label for second entry field
        self.userPass = StringVar() #define variable to store password
        passwordID = Entry(frame1, textvariable = self.userPass) #Enter userPass
        btSubmit = Button(frame1, text = "Login", command = self.submitButton) #Submit button returns info
        #design layout of login GUI
        label1.grid(row = 1, column = 1) 
        label2.grid(row = 2, column = 1)
        entryID.grid(row = 1, column = 2)
        passwordID.grid(row = 2, column = 2)
        btSubmit.grid(row = 3, column = 3)
        
        window.mainloop() #needed here now, since we will import mainGUI functions after a succesful login

    #function checks password
    def checkPassword(self): # Disabled, i can't get the string equality figured out..
    	#if repr(self.userPass) == repr(self.validPass):
    	check = True
    	#else:
    		#check = False
    	return check

    #function pulls information from user file
    #information should be ID, password, balance
    def pullUserFile(self):
    	userFile = open("users.txt", "r")
    	self.validID = str(userFile.readline())
    	self.validPass = str(userFile.readline())
    	self.userBalance = float(userFile.readline())
    	userFile.close()
    	return
    
    #function returns information given
    def submitButton(self):
        self.pullUserFile()
        if self.checkPassword():
            import mainGUI 
           # mainGUI.mainGUI() #if password checks, open mainGUI
           # WOW! you don't even need this?^^ import does it!?
        else:
            print("Invalid Password")
        #if password matches, pull balance
        #pass balance

loginGUI()
