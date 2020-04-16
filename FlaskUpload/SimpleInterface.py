import tkinter as tk
import webbrowser
import os
root = tk.Tk()
root.title("Interface")
uploaderFrame = tk.Frame(root)
downloaderFrame = tk.Frame(root)
frameList=[uploaderFrame,downloaderFrame]
for frame in frameList:
	frame.grid(row=0,column=0, sticky='news')

	frame.configure(bg='white')
def raiseFrame(frame):
	frame.tkraise()
def goToUpload():
	raiseFrame(uploaderFrame)
def goToUploadSite():
	webbrowser.open("http://192.168.1.222:5000/")
def goToDownloader():
	filenames= os.listdir("C:\\Users\\barry\\PycharmProjects\\ProjectVideos\\FlaskWebServers\\uploads")
	rowNum= 3
	for filename in filenames:
		tk.Label(downloaderFrame,text=filename,font=("Arial",40),bg="white").grid(row=rowNum,column=1,columnspan=5)
		rowNum+=1
	raiseFrame(downloaderFrame)

tk.Label(uploaderFrame,text="Uploader",font=("Arial",70),bg="white").grid(row=1,column=1,columnspan=5)
tk.Button(uploaderFrame,text="Upload File",font=("Arial",40),bg="white",command=goToUploadSite).grid(row=2,column=1)
tk.Button(uploaderFrame,text="Switch User",font=("Arial",40),bg="white",command=goToDownloader).grid(row=2,column=2)

tk.Label(downloaderFrame,text="Downloader",font=("Arial",70),bg="white").grid(row=1,column=1,columnspan=5)
tk.Label(downloaderFrame,text="All files in downloads folder:",font=("Arial",40),bg="white").grid(row=2,column=1,columnspan=5)
tk.Button(downloaderFrame,text="Switch User",font=("Arial",40),bg="white",command=goToUpload).grid(row=2,column=6)



raiseFrame(uploaderFrame)
root.mainloop()