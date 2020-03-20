import tkinter as tk
from tkinter.font import Font
import Pmw
root = tk.Tk()
root.title("Basic Interface")
Pmw.initialise(root)
interface=tk.Frame(root)
interface.configure(bg='white')
interface.grid(row=0, column=0,sticky='news')
interface.tkraise()
#Tkinter Variables
inputedData= tk.StringVar()
outputData= tk.StringVar()
#Define Functions
def Process():
	getData=inputedData.get()
	print(getData)
	outputData.set(getData)


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

#Balloons (Tooltips)
processTooltip = Pmw.Balloon(interface)
processTooltip.bind(processButton,"Process Button\nThis button will make your inputted word appear in the output section.")

entryTooltip = Pmw.Balloon(interface)
entryTooltip.bind(FirstEntry,"Please input a word.")

labelTooltip = Pmw.Balloon(interface)
labelTooltip.bind(outputLabel,"Here is your outputted word!")
root.mainloop()
