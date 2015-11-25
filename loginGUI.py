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

    #function returns information given
    def submitButton(self):
        return (userID, userPass)

