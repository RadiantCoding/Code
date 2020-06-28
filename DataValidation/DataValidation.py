import tkinter as tk

root=tk.Tk()
root.title("Error Checking Tutorial GUI")
root.configure(bg="white")
#Tkinter Variables
nameInput = tk.StringVar()
ageInput = tk.StringVar()
genderInput = tk.StringVar()
#Error Checking Functions
def PresenceCheck(input):
	if len(str(input))>0:
		return True
	else:
		print("Presence Check Failed")
		return False
def RangeCheck(input,high,low):
	if int(input)>=low and high>=int(input):
		return True
	else:
		print("Range Check Failed: "+ str(input))
		return False
def LengthCheck(input,desiredLowSize,desiredHighSize):
	if len(input)>= desiredLowSize and len(input)<= desiredHighSize:
		return True
	else:
		print("Length Check Failed: "+str(input))
		return False
def LookupCheck(input,Options):
	if input in Options:
		return True
	else:
		print("Lookup Check Failed : "+str(input))
		return False
def TypeCheck(input,datatype):
	if datatype == "str":
		if input.isalpha():
			return True
		else:
			print("Type Check Failed: "+str(input))
			return False
	if datatype == "int":
		if input.isnumeric():
			return True
		else:
			print("Type Check Failed: " + str(input))
			return False
def FormatCheck(input,mustContain):
	if mustContain in input:
		return True
	else:
		print("Format Check Failed: "+str(input))
		return False

def nameValidation(name, event = None):
	if PresenceCheck(name) and TypeCheck(name,"str"):
		if LengthCheck(name,2,20):
			print("Valid Name")
		else:
			nameEntry.configure(bg="red")
	else:
		nameEntry.configure(bg="red")

def ageValidation(age, event = None):
	if PresenceCheck(age) and TypeCheck(age,"int"):
		if RangeCheck(age,120,10):
			print("Valid Age")
		else:
			ageEntry.configure(bg="red")
	else:
		ageEntry.configure(bg="red")

def genderValidation(gender, event = None):
	if LookupCheck(gender,["Male","Female"]):
		print("Valid Gender")
	else:
		genderEntry.configure(bg="red")
		


def Reset():
	nameInput.set("")
	nameEntry.configure(bg="white")
	ageInput.set("")
	ageEntry.configure(bg="white")
	genderInput.set("")
	genderEntry.configure(bg="white")
	
tk.Label(root,text="Error Checking Tutorial",bg="white",font=("Arial",44)).grid(row=1,column=1,columnspan=5)
tk.Label(root,text="Name: ",bg="white",font=("Arial",28)).grid(row=2,column=1)
nameEntry = tk.Entry(root,textvariable=nameInput,bg="white",font=("Arial",28))
nameEntry.grid(row=2,column=2)
nameEntry.bind("<FocusOut>", lambda _: nameValidation(nameInput.get()))
tk.Label(root,text="Age: ",bg="white",font=("Arial",28),).grid(row=3,column=1)
ageEntry = tk.Entry(root,textvariable=ageInput,bg="white",font=("Arial",28))
ageEntry.grid(row=3,column=2)
ageEntry.bind("<FocusOut>", lambda _: ageValidation(ageInput.get()))
#tk.Spinbox(root,textvariable=ageInput,from_=1,to=10,font=("Arial",28),width=2).grid(row=3,column=2)
tk.Label(root,text="Gender: ",bg="white",font=("Arial",28)).grid(row=4,column=1)
#genderOptionsList = ["Male","Female"]
#genderOptionMenu = tk.OptionMenu(root,genderInput,*genderOptionsList).grid(row=4,column=2)
genderEntry=tk.Entry(root,textvariable=genderInput,bg="white",font=("Arial",28))
genderEntry.grid(row=4,column=2)
genderEntry.bind("<FocusOut>", lambda _: genderValidation(genderInput.get()))

tk.Button(root,text="Reset",font=("Arial",28),command=Reset,bg="white").grid(row=1,column=6)


root.mainloop()