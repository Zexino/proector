# -*- coding: utf-8 -*-
import datetime
from Tkinter import *
import ttk
class Data():
	def __init__(self, master):
		self.root = master
		self.frame1 = Frame(master, height = 160, width = 100)
		self.frame2 = Frame(master, height = 160, width = 100)
		self.frame1.pack(side = LEFT)
		self.frame2.pack(side = RIGHT)
		self.entry1 = StringVar()
		self.entry2 = StringVar()
		self.entry3 = StringVar()
		self.I_dont = Button(self.frame1, text = "My age", command = self.Ok)
		self.day = ttk.Combobox(self.frame1, width = 12, textvariable = self.entry1, state = "readonly")
		self.month = ttk.Combobox(self.frame1, width = 12, textvariable = self.entry2, state = "readonly")
		self.year = ttk.Combobox(self.frame1, width = 12, textvariable = self.entry3, state = "readonly")
		self.wasd = tuple(range(1, 32))
		self.month["values"] = ("Січень", "Лютий", "Березень", "Квітень", "Травень",
								"Червень", "Липень", "Серпень", "Вересень", "Жовтень",
								"Листопад", "Грудень")
		a = range(1900, 2015)
		a.reverse()
		self.move = tuple(a)
		self.now = datetime.datetime.now()
		self.day["values"] = self.wasd
		self.year["values"] = self.move
		self.day.pack(side = LEFT, padx = 10)
		self.month.pack(side = LEFT, padx = 10)
		self.year.pack(side = LEFT, padx = 10)
		self.I_dont.pack(side = LEFT, padx = 10)
	def Ok(self):
		date_now =str(self.now)
		year_now = int(date_now[0:4])
		month_now = int(date_now[5:7])
		day_now = int(date_now[8:10])
		self.month.current()
		month_user = self.month.current() + 1
		day_user = int(self.day.get())
		your_year = year_now - int(self.year.get())
		if month_user > month_now:
			your_year = your_year -1
		elif month_user == month_now:
			if day_user > day_now:
				your_year = your_year -1
		print "I am %s yaers old and %s month and %s days." %(your_year, month_user, day_user)
if __name__ == "__main__":
	master = Tk()
	master.geometry("700x200")
	app = Data(master)
	master.mainloop()