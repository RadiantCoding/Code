import tkinter as tk
from tkinter.font import Font
import mysql.connector
from tkinter import messagebox
import random
#Connecting MySQL to Python
mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="password123",
	database="testdatabase"
)
#Checking if database has connected
print(mydb)
#Define Cursor
mycursor= mydb.cursor()
userTableSQL="""CREATE TABLE IF NOT EXISTS users (userID int,username VARCHAR(255),password VARCHAR(255),stakeholder VARCHAR(255))"""
mycursor.execute(userTableSQL)
employeeTableSQL="""CREATE TABLE IF NOT EXISTS employee (employeeID int,firstname VARCHAR(255),secondname VARCHAR(255),gender VARCHAR(255),userID int)"""
mycursor.execute(employeeTableSQL)
managerTableSQL="""CREATE TABLE IF NOT EXISTS manager (managerID int,firstname VARCHAR(255),secondname VARCHAR(255),gender VARCHAR(255),userID int)"""
mycursor.execute(managerTableSQL)
menuTableSQL="""CREATE TABLE IF NOT EXISTS menu (itemID int,name VARCHAR(255),price int,tastyrating int)"""
mycursor.execute(menuTableSQL)

#Declare Root
root = tk.Tk()
root.title("Login System")
#Define Frames
loginFrame=tk.Frame(root)
registerFrame=tk.Frame(root)
managerMenuFrame=tk.Frame(root)
employeeMenuFrame=tk.Frame(root)
editMenuFrame=tk.Frame(root)
frameList=[loginFrame,registerFrame,managerMenuFrame,employeeMenuFrame,editMenuFrame]
#Configure all Frames
for frame in frameList:
	frame.grid(row=0,column=0, sticky='news')
	frame.configure(bg='white')
#Frame Raise Function
def raiseFrame(frame):
	frame.tkraise()
#Move To Reg Function
def moveToReg():
	raiseFrame(registerFrame)
def moveToLog():
	raiseFrame(loginFrame)
def register():
	#Generate UserID
	userID=random.randint(1,5000)
	#Insert Into Usertable
	userInsertSQL="""INSERT INTO users (userID,username,password,stakeholder) VALUES (%s,%s,%s,%s)"""
	mycursor.execute(userInsertSQL,(userID,inputedUsername.get(),inputedPassword.get(),inputedStakeholder.get()))
	mydb.commit()
	# Determine which table to place new user into
	if inputedStakeholder.get() == "Employee":
		employeeID=random.randint(1,5000)
		employeeInsertSQL="""INSERT INTO employee (employeeID,firstname,secondname,gender,userID) VALUES(%s,%s,%s,%s,%s)"""
		mycursor.execute(employeeInsertSQL,(employeeID,inputedFirstName.get(),inputedSecondName.get(),inputedGender.get(),userID))
		mydb.commit()
		#Clear Tkinter Vars Used
		inputedUsername.set("")
		inputedPassword.set("")
		inputedStakeholder.set("")
		inputedFirstName.set("")
		inputedSecondName.set("")
		inputedGender.set("")
		raiseFrame(loginFrame)
		messagebox.showinfo("Success", "Register Successful")
	elif inputedStakeholder.get() == "Manager":
		managerID=random.randint(1,5000)
		managerInsertSQL="""INSERT INTO manager (managerID,firstname,secondname,gender,userID) VALUES(%s,%s,%s,%s,%s)"""
		mycursor.execute(managerInsertSQL,(managerID,inputedFirstName.get(),inputedSecondName.get(),inputedGender.get(),userID))
		mydb.commit()
		#Clear Tkinter Vars Used
		inputedUsername.set("")
		inputedPassword.set("")
		inputedStakeholder.set("")
		inputedFirstName.set("")
		inputedSecondName.set("")
		inputedGender.set("")
		raiseFrame(loginFrame)
		messagebox.showinfo("Success","Register Successful")
	else:
		pass
def login():
	found=False
	usercredentialsSQL="""SELECT userID,username,password,stakeholder FROM users"""
	mycursor.execute(usercredentialsSQL)
	myusers=mycursor.fetchall()
	for user in myusers:
		if user[1] == inputedUsername.get() and user[2] == inputedPassword.get():
			found=True
			if user[3]=="Employee":
				findUserSQL="""SELECT firstname,secondname,gender FROM employee WHERE userID=%s"""
				mycursor.execute(findUserSQL,(user[0],))
				myresults=mycursor.fetchone()
				stringGreet=f"Hello Employee {myresults[0]} {myresults[1]} who is {myresults[2]}"
				employeeGreeting.set(stringGreet)
				raiseFrame(employeeMenuFrame)
				
				#Labels
			elif user[3]=="Manager":
				findUserSQL="""SELECT firstname,secondname,gender FROM manager WHERE userID=%s"""
				mycursor.execute(findUserSQL,(user[0],))
				myresults=mycursor.fetchone()
				stringGreet = f"Hello Manager {myresults[0]} {myresults[1]} who is {myresults[2]}"
				managerGreeting.set(stringGreet)
				raiseFrame(managerMenuFrame)
				#Labels
			else:
				#No Stakeholder Table Defined for this user yet.
				pass
	if found==False:
		# Invalid Username Or Password
		messagebox.showerror("ERROR", "Invalid Username Or Password!")

def delete():
	DeleteSQL="""DELETE FROM employee WHERE firstname=%s AND secondname=%s"""
	mycursor.execute(DeleteSQL,(employeeFireFName.get(),employeeFireSName.get()))
	mydb.commit()
	messagebox.showinfo("Success!","Successful Deletion")
	
def editMenuRaiseFrame():
	editItemNameList=[]
	getItemNames="""SELECT name FROM menu"""
	mycursor.execute(getItemNames)
	myresults=mycursor.fetchall()
	for result in myresults:
		editItemNameList.append(result[0])
	editMenuOptionMenu = tk.OptionMenu(editMenuFrame, editItemName, *editItemNameList)
	editMenuOptionMenu.grid(row=2,column=2)
	raiseFrame(editMenuFrame)

def optionChanged(*args):
	findMenuItemSQL="""SELECT name,price,tastyrating FROM menu WHERE name=%s"""
	mycursor.execute(findMenuItemSQL,(editItemName.get(),))
	myresult= mycursor.fetchone()
	editMenuName.set(myresult[0])
	editMenuPrice.set(myresult[1])
	editMenuTasty.set(myresult[2])

def editMenu():
	editMenuSQL="""UPDATE menu SET name=%s,price=%s,tastyrating=%s WHERE name=%s"""
	mycursor.execute(editMenuSQL,(editMenuName.get(),editMenuPrice.get(),editMenuTasty.get(),editItemName.get()))
	mydb.commit()
	messagebox.showinfo("Edit Success","Edit Successful")
	raiseFrame(managerMenuFrame)

	



	

#Tkinter Vars
inputedUsername=tk.StringVar()
inputedPassword=tk.StringVar()
inputedFirstName=tk.StringVar()
inputedSecondName=tk.StringVar()
inputedGender=tk.StringVar()
genderOptions=['Male','Female','Other']
inputedGender.set('Male')
inputedStakeholder=tk.StringVar()
stakeholderOptions=['Employee','Manager']
inputedStakeholder.set("Employee")
employeeFireFName=tk.StringVar()
employeeFireSName=tk.StringVar()
editMenuName=tk.StringVar()
editMenuPrice=tk.IntVar()
editMenuTasty=tk.IntVar()
editItemNameList=[]
editItemName=tk.StringVar()
editItemName.trace("w", optionChanged)

#Fonts
titleFont = Font(family="Arial", size="48")
labelFont = Font(family="Arial", size="24")
buttonFont =Font(family="Arial",size = "20")

#Stakeholder Menus
employeeGreeting=tk.StringVar()
employeeGreeting.set("")
managerGreeting=tk.StringVar()
managerGreeting.set("")
#Login Frame Widgets
#Labels
titleLabel=tk.Label(loginFrame,text="System Name",font=titleFont,fg='green',bg='white')
titleLabel.grid(row=1,column=1,columnspan=5)
helplogLabel=tk.Label(loginFrame,text="Fill in the fields below to Login \n or Register a new account",bg='white')
helplogLabel.grid(row=2,column=1,columnspan=5)
usernameLabel=tk.Label(loginFrame,text="Input Username: ",fg="black",font=labelFont,bg='white')
usernameLabel.grid(row=3,column=1)
passwordLabel=tk.Label(loginFrame,text="Input Password: ",fg="black",font=labelFont,bg='white')
passwordLabel.grid(row=4,column=1)
#Entry
usernameEntry=tk.Entry(loginFrame,textvariable=inputedUsername,font=labelFont)
usernameEntry.grid(row=3,column=2,columnspan=2)
passwordEntry=tk.Entry(loginFrame,textvariable=inputedPassword,font=labelFont,show='*')
passwordEntry.grid(row=4,column=2,columnspan=2)
#Buttons
loginButton=tk.Button(loginFrame,command=login,font=buttonFont,text='Login')
loginButton.grid(row=5,column=2)
moveToRegButton=tk.Button(loginFrame,command=moveToReg,font=buttonFont,text='Register')
moveToRegButton.grid(row=5,column=1)

#Register Frame Widgets
titleRegLabel=tk.Label(registerFrame,text="Register",font=titleFont,fg='green',bg='white')
titleRegLabel.grid(row=1,column=1,columnspan=5)
helpregLabel=tk.Label(registerFrame,text="Fill in the fields below to Register",bg='white')
helpregLabel.grid(row=2,column=1,columnspan=5)
firstNameLabel=tk.Label(registerFrame,text="First Name: ",fg="black",font=labelFont,bg='white')
firstNameLabel.grid(row=3,column=1)
secondNameLabel=tk.Label(registerFrame,text="Second Name: ",fg="black",font=labelFont,bg='white')
secondNameLabel.grid(row=4,column=1)
genderLabel=tk.Label(registerFrame,text="Gender: ",fg="black",font=labelFont,bg='white')
genderLabel.grid(row=5,column=1)
stakeholderLabel=tk.Label(registerFrame,text="Stakeholder: ",fg="black",font=labelFont,bg="white")
stakeholderLabel.grid(row=6,column=1)
usernameRegLabel=tk.Label(registerFrame,text="Username: ",fg="black",font=labelFont,bg='white')
usernameRegLabel.grid(row=7,column=1)
passwordRegLabel=tk.Label(registerFrame,text="Password: ",fg="black",font=labelFont,bg='white')
passwordRegLabel.grid(row=8,column=1)
#Entry Widgets
firstNameEntry=tk.Entry(registerFrame,textvariable=inputedFirstName,fg="black",font=labelFont,bg='white')
firstNameEntry.grid(row=3,column=2)
secondNameEntry=tk.Entry(registerFrame,textvariable=inputedSecondName,fg="black",font=labelFont,bg='white')
secondNameEntry.grid(row=4,column=2)
genderEntry = tk.OptionMenu(registerFrame,inputedGender,*genderOptions)
genderEntry.grid(row=5,column=2)
stakeholderEntry=tk.OptionMenu(registerFrame,inputedStakeholder,*stakeholderOptions)
stakeholderEntry.grid(row=6,column=2)
usernameRegEntry=tk.Entry(registerFrame,textvariable=inputedUsername,fg="black",font=labelFont,bg='white')
usernameRegEntry.grid(row=7,column=2)
passwordRegEntry=tk.Entry(registerFrame,textvariable=inputedPassword,fg="black",font=labelFont,bg='white',show='*')
passwordRegEntry.grid(row=8,column=2)

#Buttons
backButton=tk.Button(registerFrame,command=moveToLog,font=buttonFont,text='Back')
backButton.grid(row=9,column=1)
regButton=tk.Button(registerFrame,command=register,font=buttonFont,text='Register')
regButton.grid(row=9,column=2)


#EmployeeMenuFrame Widgets
greetingELabel=tk.Label(employeeMenuFrame,textvariable=employeeGreeting,bg="white",fg="black")
greetingELabel.grid(row=1,column=1)
greetingMLabel=tk.Label(managerMenuFrame,textvariable=managerGreeting,bg="white",fg="black")
greetingMLabel.grid(row=1,column=1)
eFName=tk.Label(managerMenuFrame,text="Employee First Name",bg='white')
eFName.grid(row=2,column=1)
eFNameEntry=tk.Entry(managerMenuFrame,textvariable=employeeFireFName,bg='white')
eFNameEntry.grid(row=2,column=2)
eSName=tk.Label(managerMenuFrame,text="Employee Second Name",bg="white")
eSName.grid(row=2,column=3)
eSNameEntry=tk.Entry(managerMenuFrame,textvariable=employeeFireSName)
eSNameEntry.grid(row=2,column=4)

deleteButton=tk.Button(managerMenuFrame,text="Fire!",bg="white",command=delete,font=labelFont)
deleteButton.grid(row=3,column=1)

editMenuButtonRaise=tk.Button(managerMenuFrame,text="Edit Menu",bg="white",command=editMenuRaiseFrame,font=labelFont)
editMenuButtonRaise.grid(row=4,column=1)

#editMenuFrame Widgets
editMenuLabel=tk.Label(editMenuFrame,text="Edit Menu",font=titleFont,fg='blue',bg='white')
editMenuLabel.grid(row=1,column=1,columnspan=5)
editMenuChoice=tk.Label(editMenuFrame,text="Choose an Item: ",fg="black",font=labelFont,bg='white')
editMenuChoice.grid(row=2,column=1)
editMenuNameLabel=tk.Label(editMenuFrame,text="Menu Item Name: ",fg="black",font=labelFont,bg='white')
editMenuNameLabel.grid(row=3,column=1)
editMenuPriceLabel=tk.Label(editMenuFrame,text="Menu Item Price £: ",fg="black",font=labelFont,bg='white')
editMenuPriceLabel.grid(row=4,column=1)
editMenuPriceLabel=tk.Label(editMenuFrame,text="Tasty Scale: ",fg="black",font=labelFont,bg='white')
editMenuPriceLabel.grid(row=5,column=1)
editMenuNameEntry=tk.Entry(editMenuFrame,textvariable=editMenuName,font=labelFont,bg='white')
editMenuNameEntry.grid(row=3,column=2)
editMenuPriceEntry=tk.Entry(editMenuFrame,textvariable=editMenuPrice,font=labelFont,bg='white')
editMenuPriceEntry.grid(row=4,column=2)
editMenuTastyScale=tk.Scale(editMenuFrame,variable=editMenuTasty,bg='white',orient=tk.HORIZONTAL)
editMenuTastyScale.grid(row=5,column=2)

editMenuButton=tk.Button(editMenuFrame,font=labelFont,command=editMenu,text="Edit")
editMenuButton.grid(row=6,column=1,columnspan=2)
raiseFrame(loginFrame)
root.mainloop()

