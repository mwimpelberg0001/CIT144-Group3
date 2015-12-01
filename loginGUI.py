from Tkinter import *
from os import path 

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
        btCreate = Button(frame1, text = "Create New User", command = self.createUser)#Button calls the createUser function
        #design layout of login GUI
        label1.grid(row = 1, column = 1) 
        label2.grid(row = 2, column = 1)
        entryID.grid(row = 1, column = 2)
        passwordID.grid(row = 2, column = 2)
        btCreate.grid(row = 4, column = 3)
        btSubmit.grid(row = 3, column = 3)
        
        window.mainloop() #needed here now, since we will import mainGUI functions after a succesful login

    #function returns information given
    def submitButton(self):
        #pull user data function
        #call the password function
        #if password matches, pull balance
        #pass balance
        return (userID, balance)
        
    #function adds a userfile to users directory, with entered username and password
    
    def createUser(self):
    	""" 
    	kept getting formatting issues "expected an indented block" so i just commented this out to make it happy for now
    	
    	userPath = "users/"
    	userPath.append(self.userID) #hopefully this will create a variable to hold our folder path for each user (users/currentUser)
    	if path.isfile(userPath):
    		#print "user already exists"
    	else:
			return
			#create the userfile with the entered username
		"""
	return


    #function checks password
    def checkPassword(self):
    	pullUserFile(self) #it will need this to compare entered password to stored one
        return

    #function pulls information from user file
    #information should be ID, password, balance
    def pullUserFile(self):
        return

    
loginGUI()
