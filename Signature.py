from tkinter import *
from PIL import Image, ImageDraw

#Create tkinter frame and canvas
tk = Tk()
tk.title("Signature Please")
cvs = Canvas(tk, width=500,height=500)
cvs.pack()

#Define internal PIL image
img = Image.new('RGB', (500,500),(255,255,255))
draw = ImageDraw.Draw(img)

#Define boolean value for mouse button pressed
mousePressed = False

last = None
#Called upon left clicking
def press(evt):
	global mousePressed
	mousePressed= True
	
#Called upon release of left click
def release(evt):
	#Save Image
	img.save('img.png')
	tk.destroy()

#Event binding
cvs.bind_all('<ButtonPress-1>', press)
cvs.bind_all('<ButtonRelease-1>',release)

#Drawing
def move(evt):
	global mousePressed, last
	x, y = evt.x,evt.y
	if mousePressed:
		#last stores the previous x,y position of the mouse on the canvas
		if last is None:
			last = (x,y)
			return
		draw.line(((x,y),last),(0,0,0))
		#Draw Line on Canvas
		cvs.create_line(x,y,last[0], last[1])
		last = (x,y)

#Calls drawing function on mouse movement
cvs.bind_all('<Motion>',move)
tk.mainloop()