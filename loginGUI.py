try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *
    
from mainGUI import *

class loginGUI:
    def __init__(self):
        self.window = Tk() #create window
        self.window.title("Python Classroom ATM") #set window title

        frame1 = Frame(self.window)
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
        
        self.window.mainloop() #needed here now, since we will import mainGUI functions after a succesful login


    #function returns information given
    def submitButton(self):
        users = [] #used to extract lines from user file
        success = [] #used to pass correct line
        with open("users.txt", "r") as inputfile: #opens the database
            for line in inputfile:  #looking through the database by line
                users.append((line.strip().split(','))) #pull database into a master list
        for ident in range(0, len(users)): #looking through the list
            if self.userID.get() == users[ident][0]: #find the user that matches given
                if self.userPass.get() == users[ident][1]: #check the password of user is good
                    for item in users[ident]: #extract that list into a seperate list
                        success.append(item)

                    name = success[0]
                    activeUser = []
                    activeUser = success
                    inputfile.close()
                    self.window.destroy()
                    mainGUI(name, activeUser) #fire up the main GUI
                else:
                    print ("Wrong password") #Password didnt match user given

loginGUI()
