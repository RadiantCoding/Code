import folium
from geopy.geocoders import Nominatim
import urllib.request
import json
import tkinter as tk
from tkinter import messagebox
from math import radians, cos, sin, asin, sqrt
import webbrowser
import os
from PIL import ImageTk, Image
import random

# Constants
INST_LAT = 54.597045
INST_LONG = -5.936478


# Obtain the dictionary of data associated with postcode.
def getLatLong(postcode):
	try:
		# request for postcode data
		res = urllib.request.urlopen("http://api.postcodes.io/postcodes/{}".format(postcode)).read()
		data = json.loads(res)
		makeMap(data)
		addtionalInfo(data)
	except Exception as e:
		print(e)
		tk.messagebox.showerror("Error!", e)


def haversine(lon1, lat1, lon2, lat2):
	"""
	Calculate the distance between two points
    on the earth (specified in decimal degrees)
    """
	# convert decimal degrees to radians
	lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
	# haversine formula
	dlon = lon2 - lon1
	dlat = lat2 - lat1
	a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
	c = 2 * asin(sqrt(a))
	# Radius of earth in kilometers is 6371
	km = 6371 * c
	km = round(km, 3)
	return km


def makeMap(data):

		m = folium.Map(
			location=[INST_LAT, INST_LONG],
			zoom_start=9,
			tiles='Stamen Terrain'
		)
		tooltip = 'Click me!'
		# make INST Marker
		folium.Marker([INST_LAT, INST_LONG], popup='<i>INST</i>', tooltip=tooltip).add_to(m)
		# make Users Marker
		folium.Marker([data["result"]["latitude"], data["result"]["longitude"]], popup='<i>User Input</i>',
					  tooltip=tooltip).add_to(m)
		# list of tuples containing lat and longs to create line
		points = [(INST_LAT, INST_LONG), (data["result"]["latitude"], data["result"]["longitude"])]
		# calculate distance between two points using Haversine Formula. Uses Km
		distance = haversine(data["result"]["longitude"], data["result"]["latitude"], INST_LONG, INST_LAT)
		folium.PolyLine(points, color="red", weight=2.5, opacity=1, tooltip=str(distance) + "km").add_to(m)
		m.save('INSTOpenDayMaps.html')
		# Auto open
		webbrowser.open('file://' + os.path.realpath('INSTOpenDayMaps.html'))

def addtionalInfo(data):
	addInfoLabel = tk.Label(root, text="Additional Info", bg=lightbluecolor, font=("Courier", 40))
	addInfoLabel.grid(row=4, column=1, columnspan=5)
	rowcount = 5
	# Create Labels for each bit of data
	for label in ("Strategic Health Authority", "Parliamentary Constituency", "Administrative/Electoral Area"):
		tk.Label(root, text=(label + ": "), bg=lightbluecolor, font=("Courier", 20)).grid(row=rowcount, column=1)
		rowcount += 1
	
	SHAEntry = tk.Label(root, textvariable=SHAVar, bg=lightbluecolor, font=("Courier", 20), width=40)
	SHAEntry.grid(row=5, column=2)
	PCEntry = tk.Label(root, textvariable=PCVar, bg=lightbluecolor, font=("Courier", 20), width=40)
	PCEntry.grid(row=6, column=2)
	AEntry = tk.Label(root, textvariable=AVar, bg=lightbluecolor, font=("Courier", 20), width=40)
	AEntry.grid(row=7, column=2)
	SHAVar.set(data["result"]["nhs_ha"])
	PCVar.set(data["result"]["parliamentary_constituency"])
	AVar.set(data["result"]["admin_ward"])


# color
lightbluecolor = '#%02x%02x%02x' % (93, 188, 210)
root = tk.Tk()
root.title("RBAI Open Day Map Application")
root.configure(bg=lightbluecolor)
# Tkinter Variables
inputtedPostcode = tk.StringVar()
SHAVar = tk.StringVar()
PCVar = tk.StringVar()
AVar = tk.StringVar()
mode = tk.IntVar()
# Images
ukImg = ImageTk.PhotoImage(Image.open("uk.jpg"))

titleLabel = tk.Label(root, text="RBAI Open Day Map Application", bg=lightbluecolor, font=("Courier", 40))
titleLabel.grid(row=0, column=1, columnspan=5)
imageLabel = tk.Label(root, image=ukImg, bg=lightbluecolor, fg=lightbluecolor)
imageLabel.grid(row=1, column=1, columnspan=5)
postcodeLabel = tk.Label(root, text="Enter Postcode: ", bg=lightbluecolor, font=("Courier", 20))
postcodeLabel.grid(row=2, column=1)
postcodeEntry = tk.Entry(root, textvariable=inputtedPostcode, font=("Courier", 20))
postcodeEntry.grid(row=2, column=2)
generateButton = tk.Button(root, text="Generate!", bg="white", font=("Courier", 20),
						   command=lambda: getLatLong(inputtedPostcode.get()))
generateButton.grid(row=3, column=2)

root.mainloop()