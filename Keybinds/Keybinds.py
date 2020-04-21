import tkinter as tk
from tkinter.font import Font

root = tk.Tk()
root.title("Basic Interface")
interface=tk.Frame(root)
interface.configure(bg='white')
interface.grid(row=0, column=0,sticky='news')
interface.tkraise()
#Tkinter Variables
inputedData= tk.StringVar()
outputData= tk.StringVar()
#Define Functions
def Process(event):
	getData=inputedData.get()
	print(getData)
	outputData.set(getData)
	
	print(event.time)
	print(event.char)
	print(event.type)
	print(event.widget)
	print(event.x)
	print(event.y)

def ColorChange(event):
	if str(event.type) == "Enter":
		FirstEntry.configure(bg="lightblue")
	elif str(event.type) == "Leave":
		FirstEntry.configure(bg="white")
	else:
		pass
	

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
FirstEntry.bind("<Enter>",ColorChange)
FirstEntry.bind("<Leave>",ColorChange)

#Buttons
processButton=tk.Button(interface,text="Process",fg="black",font=buttonFont,bg='white')
processButton.bind("<Leave>",Process)
processButton.grid(row=4,column=2)
root.mainloop()
