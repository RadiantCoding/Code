import tkinter as tk
import Pmw
root = tk.Tk()
Pmw.initialise(root)
root.title("Counter App")
myFrame = tk.Frame(root)
myFrame.grid(row=1,column=1,columnspan=5)
myFrame.configure(bg='pink')
#Integer counter
counter = Pmw.Counter(myFrame)
counter.setentry(10)
#add
counter.increment()
#subtract
counter.decrement()
counter.grid(row=1,column=1)
#time counter, counts minutes and is vertical
timeCounter = Pmw.Counter(myFrame,datatype = "time",increment=60,orient="vertical")
timeCounter.setentry("00:00:00")
timeCounter.grid(row=2,column=1)
timeCounter.configure(
	downarrow_background= 'purple',
	uparrow_background = 'blue',
	hull_relief = 'sunken',
	hull_borderwidth=5,
)
tk.Label(myFrame,text="I am in MyFrame \n The hull is the frame keeping the widgets making up the mega widget together").grid(row=3,column=1)
root.mainloop()