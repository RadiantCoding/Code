import calendar
import datetime
import sys

#imports correct version of tkinter based on python version
if sys.version[0] == '2':
	import Tkinter as tk
else:
	import tkinter as tk


class Calendar:
	#Instantiation
	def __init__(self, parent, values):
		self.values = values
		self.parent = parent
		self.cal = calendar.TextCalendar(calendar.SUNDAY)
		self.year = datetime.date.today().year
		self.month = datetime.date.today().month
		self.wid = []
		self.day_selected = 1
		self.month_selected = self.month
		self.year_selected = self.year
		self.day_name = ''
		
		self.setup(self.year, self.month)
		
	#Resets the buttons
	def clear(self):
		for w in self.wid[:]:
			w.grid_forget()
			# w.destroy()
			self.wid.remove(w)
			
	#Moves to previous month/year on calendar
	def go_prev(self):
		if self.month > 1:
			self.month -= 1
		else:
			self.month = 12
			self.year -= 1
		# self.selected = (self.month, self.year)
		self.clear()
		self.setup(self.year, self.month)
	
	# Moves to next month/year on calendar
	def go_next(self):
		if self.month < 12:
			self.month += 1
		else:
			self.month = 1
			self.year += 1
		
		# self.selected = (self.month, self.year)
		self.clear()
		self.setup(self.year, self.month)
	
	#Called on date button press
	def selection(self, day, name):
		self.day_selected = day
		self.month_selected = self.month
		self.year_selected = self.year
		self.day_name = name
		
		# Obtaining data
		self.values['day_selected'] = day
		self.values['month_selected'] = self.month
		self.values['year_selected'] = self.year
		self.values['day_name'] = name
		self.values['month_name'] = calendar.month_name[self.month_selected]
		
		self.clear()
		self.setup(self.year, self.month)
	
	def setup(self, y, m):
		#Tkinter creation
		left = tk.Button(self.parent, text='<', command=self.go_prev)
		self.wid.append(left)
		left.grid(row=0, column=1)
		
		header = tk.Label(self.parent, height=2, text='{}   {}'.format(calendar.month_abbr[m], str(y)))
		self.wid.append(header)
		header.grid(row=0, column=2, columnspan=3)
		
		right = tk.Button(self.parent, text='>', command=self.go_next)
		self.wid.append(right)
		right.grid(row=0, column=5)
		
		days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
		for num, name in enumerate(days):
			t = tk.Label(self.parent, text=name[:3])
			self.wid.append(t)
			t.grid(row=1, column=num)
		
		for w, week in enumerate(self.cal.monthdayscalendar(y, m), 2):
			for d, day in enumerate(week):
				if day:
					# print(calendar.day_name[day])
					b = tk.Button(self.parent, width=1, text=day,
								  command=lambda day=day: self.selection(day, calendar.day_name[(day) % 7]))
					self.wid.append(b)
					b.grid(row=w, column=d)
		
		sel = tk.Label(self.parent, height=2, text='{} {} {} {}'.format(
			self.day_name, calendar.month_name[self.month_selected], self.day_selected, self.year_selected))
		self.wid.append(sel)
		sel.grid(row=8, column=0, columnspan=7)
		
		ok = tk.Button(self.parent, width=5, text='OK', command=self.kill_and_save)
		self.wid.append(ok)
		ok.grid(row=9, column=2, columnspan=3, pady=10)
	#Quit out of the calendar and terminate tkinter instance.
	def kill_and_save(self):
		self.parent.destroy()
