import tkinter as tk
from tkinter.font import Font

root = tk.Tk()
root.title("Basic Interface")
root.configure(bg="white")
interface=tk.Frame(root)
signUp=tk.Frame(root)
menu=tk.Frame(root)
frameList=[interface,signUp]
for frame in frameList:
	frame.configure(bg="white")
	frame.grid(row=1,column=1,sticky="news")
	
menu.configure(bg="grey")
menu.grid(row=1,column=0)

interface.tkraise()
def raiseFrame(frame):
	frame.tkraise()
#Tkinter Variables
inputedData= tk.StringVar()
outputData= tk.StringVar()
#Define Functions
def Process():
	getData=inputedData.get()
	print(getData)
	outputData.set(getData)

def goToSignup():
	raiseFrame(signUp)

def goToProcess():
	raiseFrame(interface)


#Fonts
titleFont = Font(family="Arial", size="48")
labelFont = Font(family="Arial", size="24")
buttonFont = Font(family="Arial",size = "20")
#Labels
titleLabel=tk.Label(interface,text="Interface Title",fg="black",font=titleFont,bg='white')
titleLabel.grid(row=1,column=1,columnspan=5)
inputLabel=tk.Label(interface,text="Input Data: ",fg="black",font=labelFont,bg='white')
inputLabel.grid(row=2,column=1)
oLabel=tk.Label(interface,text="Output Data: ",fg="black",font=labelFont,bg='white')
oLabel.grid(row=3,column=1)
outputLabel=tk.Label(interface,textvariable=outputData,fg="black",font=labelFont,bg='white')
outputLabel.grid(row=3,column=2)
#Entry Boxes
FirstEntry=tk.Entry(interface,textvariable=inputedData,font=labelFont)
FirstEntry.grid(row=2,column=2,columnspan=2)

#Buttons
processButton=tk.Button(interface,text="Process",command=Process,fg="black",font=buttonFont,bg='white')
processButton.grid(row=4,column=2)

#Signup Menu
tk.Label(signUp,text="Sign up",fg="black",font=titleFont,bg="white").grid(row=1,column=1,columnspan=5)
tk.Label(signUp,text="Username",fg="black",font=buttonFont,bg="white").grid(row=2,column=1)
tk.Entry(signUp,font=labelFont,bg="white").grid(row=2,column=2)

#Time
timeSelectFrame = tk.Frame(signUp,borderwidth=5,bg="lightblue")
timeSelectFrame.grid(row=1,column=7)
tk.Spinbox(timeSelectFrame,from_=1, to=24,bg="lightblue",width=2).grid(row=1,column=1)
tk.Label(timeSelectFrame,text=":",bg="lightblue").grid(row=1,column=2)
tk.Spinbox(timeSelectFrame,values=(0,15,30,45),bg="lightblue",width=2).grid(row=1,column=3)
#13:00

#Nav Menu
tk.Label(menu,text="Navigation",fg="black",bg="grey",font=titleFont).grid(row=1,column=1,columnspan=3)
tk.Button(menu,text="Process",fg="black",font=buttonFont,bg="grey",command=goToProcess).grid(row=2,column=1)
tk.Button(menu,text="Sign Up",fg="black",font=buttonFont,bg="grey",command=goToSignup).grid(row=3,column=1)
root.mainloop()