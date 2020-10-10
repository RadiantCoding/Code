import tkinter as tk
from tkinter import scrolledtext
#Declare Root
root = tk.Tk()
root.title("Scrolltext Widget")
tk.Label(root,text="My Scrolled Text Widget",font=("Times New Roman",25))\
	.grid(row=0,column=1)
#Define ScrollTextWidget
#wrap keyword used to wrap around text
myScrollTextWidget = scrolledtext.ScrolledText(root,wrap=tk.WORD,width=50,height=20,font=("Times New Roman",15))
myScrollTextWidget.grid(row=1,column=1)
def printToConsole():
	print(myScrollTextWidget.get("1.0","end-1c"))
#Buttons
myButton = tk.Button(root,text="Print to console!",command=printToConsole).grid(row=2,column=1)
myScrollTextWidget.insert(tk.INSERT, "Hello")

root.mainloop()