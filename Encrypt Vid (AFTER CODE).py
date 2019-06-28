import tkinter as tk
from tkinter.font import Font
from cryptography.fernet import Fernet
import mysql.connector
import csv
import random
# Connect MySQL
if True:
	mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="password123",
		database="cafefishdb"
	)
mycursor=mydb.cursor()
#Create Table
mycursor.execute("""CREATE TABLE IF NOT EXISTS usercredentials(username VARCHAR(255),password VARCHAR(255),userID int)""")
mycursor.execute("""CREATE TABLE IF NOT EXISTS customer(userID int,firstname VARCHAR(255),secondname VARCHAR(255))""")
#Obtaining Encryption Key
#Open Text File
with open("Keys.txt","r") as csvfile:
	reader=csv.reader(csvfile)
	KeyFound=0
	for row in reader:
		try:
			print(row[0])
		except IndexError:
			continue
		if len(row[0])>4:
			KeyFound=1
			Key=row[0]
		else:
			pass
if KeyFound==0:
	Key= Fernet.generate_key()
	csvfile.close()
if KeyFound==0:
	with open("Keys.txt","w") as csvfile:
		headers =['key']
		writer = csv.DictWriter(csvfile,fieldnames=headers)
		writer.writeheader()
		writer.writerow({'key': Key.decode('utf-8')})
		csvfile.close()

print(Key)
Ecy = Fernet(Key)
csvfile.close()

#Declare Root
root = tk.Tk()
root.title("Login System")
#Define Frames
loginFrame=tk.Frame(root)
registerFrame=tk.Frame(root)
customerFrame=tk.Frame(root)
frameList=[loginFrame,registerFrame,customerFrame]
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

def login():
	mycursor.execute("SELECT * FROM usercredentials")
	myresults=mycursor.fetchall()
	for record in myresults:
		b = bytes(record[1], 'utf-8')
		decryptedPassword=str(Ecy.decrypt(b))
		decryptedPassword = decryptedPassword.strip("b'")
		print("Password:")
		print(decryptedPassword)
		if inputedPassword.get()==decryptedPassword and inputedUsername.get()==record[0]:
			selectData="SELECT firstname,secondname FROM customer WHERE userID=%s"
			mycursor.execute(selectData,(record[2],))
			myresults=mycursor.fetchone()
			tempVar="Welcome",myresults[0],myresults[1]
			greetings.set(tempVar)
			raiseFrame(customerFrame)
		else:
			print("Not Found")
	pass
	
def register():
	userID=random.randint(1,5000)
	b = bytes(inputedPassword.get(),'utf-8')
	encryptedPassword = Ecy.encrypt(b)
	userInsert="""INSERT INTO usercredentials (username,password,userID) VALUES(%s,%s,%s)"""
	mycursor.execute(userInsert,(inputedUsername.get(),encryptedPassword,userID))
	mydb.commit()
	custInsert="""INSERT INTO customer (userID,firstname,secondname) VALUES (%s,%s,%s)"""
	mycursor.execute(custInsert,(userID,inputedFirstName.get(),inputedSecondName.get()))
	mydb.commit()
	raiseFrame(loginFrame)
	inputedFirstName.set("")
	inputedSecondName.set("")
	inputedUsername.set("")
	inputedPassword.set("")
	
#Tkinter Vars
inputedUsername=tk.StringVar()
inputedPassword=tk.StringVar()
inputedFirstName=tk.StringVar()
inputedSecondName=tk.StringVar()
greetings=tk.StringVar()
greetings.set("")
#Fonts
titleFont = Font(family="Arial", size="48")
labelFont = Font(family="Arial", size="24")
buttonFont =Font(family="Arial",size = "20")

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
usernameRegLabel=tk.Label(registerFrame,text="Username: ",fg="black",font=labelFont,bg='white')
usernameRegLabel.grid(row=5,column=1)
passwordRegLabel=tk.Label(registerFrame,text="Password: ",fg="black",font=labelFont,bg='white')
passwordRegLabel.grid(row=6,column=1)
#Entry Widgets
firstNameLabel=tk.Entry(registerFrame,textvariable=inputedFirstName,fg="black",font=labelFont,bg='white')
firstNameLabel.grid(row=3,column=2)
secondNameLabel=tk.Entry(registerFrame,textvariable=inputedSecondName,fg="black",font=labelFont,bg='white')
secondNameLabel.grid(row=4,column=2)
usernameRegLabel=tk.Entry(registerFrame,textvariable=inputedUsername,fg="black",font=labelFont,bg='white')
usernameRegLabel.grid(row=5,column=2)
passwordRegLabel=tk.Entry(registerFrame,textvariable=inputedPassword,fg="black",font=labelFont,bg='white',show='*')
passwordRegLabel.grid(row=6,column=2)
#Buttons
backButton=tk.Button(registerFrame,command=moveToLog,font=buttonFont,text='Back')
backButton.grid(row=7,column=1)
regButton=tk.Button(registerFrame,command=register,font=buttonFont,text='Register')
regButton.grid(row=7,column=2)

#Customer Frame Widgets
titleCLabel=tk.Label(customerFrame,textvariable=greetings,font=titleFont,fg='green',bg='white')
titleCLabel.grid(row=1,column=1,columnspan=5)

raiseFrame(loginFrame)
root.mainloop()

