#Ensure you have imported ttk
from tkinter import ttk
#Defining The Treeview Widget
EmployView=ttk.Treeview(FRAME NAME)
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

#Update Function
def treeviewEmployeeUpdate():
	# Delete Everything From Treeview
	Remove = EmployView.get_children()
	for child in Remove:
		EmployView.delete(child)
	# SELECT data from table
	mycursor.execute("SELECT firstname,secondname,gender,jobtype,hourlywage FROM employee")
	myresults = mycursor.fetchall()
	#Insert obtained data into treeview widget
	for i in myresults:
		EmployView.insert("", "end", text="", values=(i[0], i[1], i[2], i[3], i[4]))

#Call the function:
treeviewEmployeeUpdate()
#Remember you do not need to update the treeview when RETRIEVING data from a table.
#You must update the treeview when;CREATING,UPDATING or DELETING from a table.