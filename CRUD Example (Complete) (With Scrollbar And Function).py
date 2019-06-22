import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font
from tkinter import scrolledtext
from tkinter import ttk
import mysql.connector
import random
#mydb definition
# Connect MySQL
if True:
	mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="password123",
		database="cafefishdb"
	)

# Outputs Connection Object
print(mydb)
mycursor = mydb.cursor()
#Create mysql
mycursor.execute("""CREATE TABLE IF NOT EXISTS employee(employeeID int ,firstname VARCHAR(255),secondname VARCHAR(255),gender VARCHAR(255),jobtype VARCHAR(255),hourlywage int)""")
#import mysql.connector
root=tk.Tk()
root.title("Cafe Fish System")
#Define Frames
treeviewFrame=tk.Frame(root)
createFrame=tk.Frame(root)
retrieveFrame=tk.Frame(root)
updateFrame=tk.Frame(root)
deleteFrame=tk.Frame(root)

#Define Frame List
frameList=[treeviewFrame,createFrame,updateFrame,retrieveFrame,deleteFrame]
#Configure all Frames
for frame in frameList:
	frame.grid(row=0,column=0, sticky='news')
	frame.configure(bg='lightblue')

def raiseFrame(frame):
	frame.tkraise()
def raiseBack():
	#Clear Variables
	firstName.set("")
	secondName.set("")
	gender.set("")
	wage.set(0.00)
	job.set("Frycook")
	treeviewEmployeeUpdate()
	treeviewFrame.tkraise()
def raiseCreate():
	job.set("Frycook")
	gender.set("Male")
	createFrame.tkraise()
def raiseRetrieve():
	nameList=[]
	mycursor.execute("""SELECT firstname,secondname FROM employee""")
	myresults=mycursor.fetchall()
	for i in myresults:
		name=i[0]+" "+i[1]
		nameList.append(name)
	searchOM = tk.OptionMenu(retrieveFrame, searchTerm, *nameList)
	searchOM.grid(row=2, column=2)
	retrieveFrame.tkraise()
def raiseUpdate():
	nameList=[]
	mycursor.execute("""SELECT firstname,secondname FROM employee""")
	myresults=mycursor.fetchall()
	for i in myresults:
		name=i[0]+" "+i[1]
		nameList.append(name)
	searchOM = tk.OptionMenu(updateFrame, updateTerm, *nameList)
	searchOM.grid(row=2, column=2)
	job.set("Frycook")
	gender.set("Male")
	updateFrame.tkraise()
def raiseDelete():
	nameList=[]
	mycursor.execute("""SELECT firstname,secondname FROM employee""")
	myresults=mycursor.fetchall()
	for i in myresults:
		name=i[0]+" "+i[1]
		nameList.append(name)
	searchOM = tk.OptionMenu(deleteFrame, deleteTerm, *nameList)
	searchOM.grid(row=2, column=2)
	deleteFrame.tkraise()

#SQL
def create():
	employeeID=random.randint(1,5000)
	insertSQL="""INSERT INTO employee (employeeID,firstname,secondname,gender,jobtype,hourlywage) VALUES(%s,%s,%s,%s,%s,%s)"""
	mycursor.execute(insertSQL,(employeeID,firstName.get(),secondName.get(),gender.get(),job.get(),wage.get()))
	mydb.commit()
	treeviewEmployeeUpdate()
	pass
def retrieve():
	fName,sName=searchTerm.get().split(" ")
	selectSQL="""SELECT firstname,secondname,gender,jobtype,hourlywage FROM employee WHERE firstname=%s AND secondname=%s"""
	mycursor.execute(selectSQL,(fName,sName))
	myresult=mycursor.fetchone()
	print(myresult)
	firstName.set(myresult[0])
	secondName.set(myresult[1])
	gender.set(myresult[2])
	job.set(myresult[3])
	wage.set(myresult[4])
	pass
def update():
	fName,sName=updateTerm.get().split(" ")
	updateSQL="""UPDATE employee SET firstname=%s,secondname=%s,gender=%s,jobtype=%s,hourlywage=%s WHERE firstname=%s AND secondname=%s"""
	mycursor.execute(updateSQL,(firstName.get(),secondName.get(),gender.get(),job.get(),wage.get(),fName,sName))
	mydb.commit()
	treeviewEmployeeUpdate()
	pass
def delete():
	fName,sName=deleteTerm.get().split(" ")
	deleteSQL="""DELETE FROM employee WHERE firstname=%s AND secondname=%s"""
	mycursor.execute(deleteSQL,(fName,sName))
	mydb.commit()
	treeviewEmployeeUpdate()
	pass

def fillEntryFields(a,b,c):
	fName,sName=updateTerm.get().split(" ")
	SQL="""SELECT firstname,secondname,gender,jobtype,hourlywage FROM employee WHERE firstname=%s AND secondname=%s"""
	mycursor.execute(SQL,(fName,sName))
	myresults=mycursor.fetchone()
	firstName.set(myresults[0])
	secondName.set(myresults[1])
	gender.set(myresults[2])
	job.set(myresults[3])
	wage.set(myresults[4])

def treeviewEmployeeUpdate():
	#Delete Everything From Treeview
	Remove = EmployView.get_children()
	for child in Remove:
		EmployView.delete(child)
	#Input New Data Into Treeview Widget
	mycursor.execute("SELECT firstname,secondname,gender,jobtype,hourlywage FROM employee")
	myresults=mycursor.fetchall()
	for i in myresults:
		EmployView.insert("","end",text="",values=(i[0],i[1],i[2],i[3],i[4]))

def fireEmployee():
	items=EmployView.selection()
	print(items)
	employeeData=[]
	for i in items:
		employeeData.append(EmployView.item(i)['values'])
	print(employeeData)
	for employee in employeeData:
		fireEmployeeSQL="""DELETE FROM employee WHERE firstname=%s AND secondname=%s"""
		mycursor.execute(fireEmployeeSQL,(employee[0],employee[1]))
		print("Deleted",employee[0],employee[1])
		mydb.commit()
		
#Tkinter Variable
firstName=tk.StringVar()
secondName=tk.StringVar()
gender=tk.StringVar()
wage=tk.StringVar()
job=tk.StringVar()

searchTerm=tk.StringVar()
deleteTerm=tk.StringVar()
updateTerm=tk.StringVar()
updateTerm.trace('w',fillEntryFields)
#Setting Default Values
firstName.set("")
secondName.set("")
gender.set("")
wage.set(0.00)
job.set("Frycook")
#Fonts
titleFont = Font(family="Arial", size="48")
labelFont = Font(family="Arial", size="24")
buttonFont = Font(family="Arial",size = "20")
#treeview Frame Widgets Define
EmployView=ttk.Treeview(treeviewFrame)
EmployView['columns']=("firstname","secondname","gender","jobtype","hourlywage")
EmployView.grid(row=2,column=1,columnspan=5)
EmployView.heading("#0",text="",anchor="w")
EmployView.column("#0",anchor="center",width=5,stretch=tk.NO)
EmployView.heading("firstname",text="First Name",anchor="w")
EmployView.column("firstname",anchor="center",width=80)
EmployView.heading("secondname",text="Second Name",anchor="w")
EmployView.column("secondname",anchor="center",width=80)
EmployView.heading("gender",text="Gender",anchor="w")
EmployView.column("gender",anchor="center",width=80)
EmployView.heading("jobtype",text="Job Type",anchor="w")
EmployView.column("jobtype",anchor="center",width=80)
EmployView.heading("hourlywage",text="Hourly Wage",anchor="w")
EmployView.column("hourlywage",anchor="center",width=80)
EmployViewScrollbar=ttk.Scrollbar(treeviewFrame,orient="vertical",command=EmployView.yview)
EmployView.configure(yscroll=EmployViewScrollbar.set)
EmployViewScrollbar.grid(row=2,column=6,sticky="ns")
EmployView.bind("<Return>",lambda e: fireEmployee())



#Labels
titleLabel=tk.Label(treeviewFrame,text="Cafe Fish Employee Table",font=titleFont,bg='blue',fg='lightblue')
titleLabel.grid(row=1,column=1,columnspan=5)
#Buttons
createButton=tk.Button(treeviewFrame,text="Create",font=buttonFont,bg='blue',fg='lightblue',command=raiseCreate)
createButton.grid(row=3,column=1)
retrieveButton=tk.Button(treeviewFrame,text="Retrieve",font=buttonFont,bg='blue',fg='lightblue',command=raiseRetrieve)
retrieveButton.grid(row=3,column=2)
updateButton=tk.Button(treeviewFrame,text="Update",font=buttonFont,bg='blue',fg='lightblue',command=raiseUpdate)
updateButton.grid(row=3,column=3)
deleteButton=tk.Button(treeviewFrame,text="Delete",font=buttonFont,bg='blue',fg='lightblue',command=raiseDelete)
deleteButton.grid(row=3,column=4)

#Create Frame Widgets
#createFrame
createTLabel=tk.Label(createFrame,text="Create Record In Table",font=titleFont,bg='lightblue',fg='blue')
createTLabel.grid(row=1,column=1,columnspan=5)
createFNameLabel=tk.Label(createFrame,text="First Name: ",font=labelFont,bg='lightblue',fg='blue')
createFNameLabel.grid(row=2,column=1)
createSNameLabel=tk.Label(createFrame,text="Second Name: ",font=labelFont,bg='lightblue',fg='blue')
createSNameLabel.grid(row=3,column=1)
createGenderLabel=tk.Label(createFrame,text="Gender: ",font=labelFont,bg='lightblue',fg='blue')
createGenderLabel.grid(row=4,column=1)
createJobTypeLabel=tk.Label(createFrame,text="Job Type: ",font=labelFont,bg='lightblue',fg='blue')
createJobTypeLabel.grid(row=5,column=1)
createHourlyWageLabel=tk.Label(createFrame,text="Hourly Wage £: ",font=labelFont,bg='lightblue',fg='blue')
createHourlyWageLabel.grid(row=6,column=1)
#Label Widgets
createFNameLabel=tk.Entry(createFrame,textvariable=firstName,font=labelFont,bg='lightblue',fg='blue')
createFNameLabel.grid(row=2,column=2)
createSNameLabel=tk.Entry(createFrame,textvariable=secondName,font=labelFont,bg='lightblue',fg='blue')
createSNameLabel.grid(row=3,column=2)
createWageLabel=tk.Entry(createFrame,textvariable=wage,font=labelFont,width=5,bg='lightblue',fg='blue')
createWageLabel.grid(row=6,column=2)
createGenderRBM=tk.Radiobutton(createFrame, text="Male",variable=gender,value="Male",font=labelFont,bg='lightblue',fg='blue')
createGenderRBM.grid(row=4,column=2)
createGenderRBF=tk.Radiobutton(createFrame, text="Female",variable=gender,value="Female",font=labelFont,bg='lightblue',fg='blue')
createGenderRBF.grid(row=4,column=3)
jobList=["Frycook","Register","Waiter","Stock Manager"]
createJobTypeOM=tk.OptionMenu(createFrame,job,*jobList)
createJobTypeOM.grid(row=5,column=2)
#Button
createcButton=tk.Button(createFrame,text="Create",command=create,font=buttonFont,bg="blue",fg="lightblue")
createcButton.grid(row=7,column=2)
backCButton=tk.Button(createFrame,text="Back",command=raiseBack,font=labelFont,bg="blue",fg="lightblue")
backCButton.grid(row=7,column=1)

#Retrieve Frame Widgets
#retrieveFrame
retrieveTLabel=tk.Label(retrieveFrame,text="Retrieve Record In Table",font=titleFont,bg='lightblue',fg='blue')
retrieveTLabel.grid(row=1,column=1,columnspan=5)
retrieveSearchLabel=tk.Label(retrieveFrame,text="Search Name: ",font=labelFont,bg='lightblue',fg='blue')
retrieveSearchLabel.grid(row=2,column=1)
retrieveFNameLabel=tk.Label(retrieveFrame,text="First Name: ",font=labelFont,bg='lightblue',fg='blue')
retrieveFNameLabel.grid(row=3,column=1)
retrieveSNameLabel=tk.Label(retrieveFrame,text="Second Name: ",font=labelFont,bg='lightblue',fg='blue')
retrieveSNameLabel.grid(row=4,column=1)
retrieveGenderLabel=tk.Label(retrieveFrame,text="Gender: ",font=labelFont,bg='lightblue',fg='blue')
retrieveGenderLabel.grid(row=5,column=1)
retrieveJobTypeLabel=tk.Label(retrieveFrame,text="Job Type: ",font=labelFont,bg='lightblue',fg='blue')
retrieveJobTypeLabel.grid(row=6,column=1)
retrieveHourlyWageLabel=tk.Label(retrieveFrame,text="Hourly Wage £: ",font=labelFont,bg='lightblue',fg='blue')
retrieveHourlyWageLabel.grid(row=7,column=1)
#Retrieved Data Label Widgets
retrieveFNameLabelData=tk.Label(retrieveFrame,textvariable=firstName,font=labelFont,bg='lightblue',fg='blue')
retrieveFNameLabelData.grid(row=3,column=2)
retrieveSNameLabelData=tk.Label(retrieveFrame,textvariable=secondName,font=labelFont,bg='lightblue',fg='blue')
retrieveSNameLabelData.grid(row=4,column=2)
retrieveWageLabelData=tk.Label(retrieveFrame,textvariable=wage,font=labelFont,width=5,bg='lightblue',fg='blue')
retrieveWageLabelData.grid(row=7,column=2)
retrieveGenderLabelData=tk.Label(retrieveFrame,textvariable=gender,font=labelFont,bg='lightblue',fg='blue')
retrieveGenderLabelData.grid(row=5,column=2)
jobList=["Frycook","Register","Waiter","Stock Manager"]
retrieveJobTypeOM=tk.OptionMenu(retrieveFrame,job,*jobList)
retrieveJobTypeOM.grid(row=6,column=2)
#Button
retrievecButton=tk.Button(retrieveFrame,text="Retrieve",command=retrieve,font=buttonFont,bg="blue",fg="lightblue")
retrievecButton.grid(row=8,column=2)
backCButton=tk.Button(retrieveFrame,text="Back",command=raiseBack,font=labelFont,bg="blue",fg="lightblue")
backCButton.grid(row=8,column=1)

#Update Frame Widgets
#updateFrame
updateTLabel=tk.Label(updateFrame,text="Update Record In Table",font=titleFont,bg='lightblue',fg='blue')
updateTLabel.grid(row=1,column=1,columnspan=5)
updateSearchNameLabel=tk.Label(updateFrame,text="Search Name: ",font=labelFont,bg='lightblue',fg='blue')
updateSearchNameLabel.grid(row=2,column=1)
updateFNameLabel=tk.Label(updateFrame,text="First Name: ",font=labelFont,bg='lightblue',fg='blue')
updateFNameLabel.grid(row=3,column=1)
updateSNameLabel=tk.Label(updateFrame,text="Second Name: ",font=labelFont,bg='lightblue',fg='blue')
updateSNameLabel.grid(row=4,column=1)
updateGenderLabel=tk.Label(updateFrame,text="Gender: ",font=labelFont,bg='lightblue',fg='blue')
updateGenderLabel.grid(row=5,column=1)
updateJobTypeLabel=tk.Label(updateFrame,text="Job Type: ",font=labelFont,bg='lightblue',fg='blue')
updateJobTypeLabel.grid(row=6,column=1)
updateHourlyWageLabel=tk.Label(updateFrame,text="Hourly Wage £: ",font=labelFont,bg='lightblue',fg='blue')
updateHourlyWageLabel.grid(row=7,column=1)
#Label Widgets
updateFNameLabel=tk.Entry(updateFrame,textvariable=firstName,font=labelFont,bg='lightblue',fg='blue')
updateFNameLabel.grid(row=3,column=2)
updateSNameLabel=tk.Entry(updateFrame,textvariable=secondName,font=labelFont,bg='lightblue',fg='blue')
updateSNameLabel.grid(row=4,column=2)
updateWageLabel=tk.Entry(updateFrame,textvariable=wage,font=labelFont,width=5,bg='lightblue',fg='blue')
updateWageLabel.grid(row=7,column=2)
updateGenderRBM=tk.Radiobutton(updateFrame, text="Male",variable=gender,value="Male",font=labelFont,bg='lightblue',fg='blue')
updateGenderRBM.grid(row=5,column=2)
updateGenderRBF=tk.Radiobutton(updateFrame, text="Female",variable=gender,value="Female",font=labelFont,bg='lightblue',fg='blue')
updateGenderRBF.grid(row=5,column=3)
jobList=["Frycook","Register","Waiter","Stock Manager"]
updateJobTypeOM=tk.OptionMenu(updateFrame,job,*jobList)
updateJobTypeOM.grid(row=6,column=2)
#Button
updatecButton=tk.Button(updateFrame,text="Update",command=update,font=buttonFont,bg="blue",fg="lightblue")
updatecButton.grid(row=8,column=2)
backUButton=tk.Button(updateFrame,text="Back",command=raiseBack,font=labelFont,bg="blue",fg="lightblue")
backUButton.grid(row=8,column=1)

#Delete Frame Widgets
#deleteFrame
#Labels
updateTLabel=tk.Label(deleteFrame,text="Delete Record In Table",font=titleFont,bg='lightblue',fg='blue')
updateTLabel.grid(row=1,column=1,columnspan=5)
deleteLabel=tk.Label(deleteFrame,text="Delete: ",font=labelFont,bg='lightblue',fg='blue')
deleteLabel.grid(row=2,column=1)
deleteButton=tk.Button(deleteFrame,text="Delete",command=delete,font=buttonFont,bg="blue",fg="lightblue")
deleteButton.grid(row=2,column=3)
backUButton=tk.Button(deleteFrame,text="Back",command=raiseBack,font=labelFont,bg="blue",fg="lightblue")
backUButton.grid(row=3,column=3)

#Updates Treeview on Initial Startup
treeviewEmployeeUpdate()
raiseFrame(treeviewFrame)
root.mainloop()

