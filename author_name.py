# -*- coding: utf-8 -*-
from Tkinter import * 
import ttk 
import sqlite3 
class Author():
	def __init__(self, master):
		self.root = master
		"""Додає вже раніше створену датабазу до програми для подальшого використання"""
		self.conn = sqlite3.connect('chinook.db')
		self.c = self.conn.cursor()
		
		self.bigframe = Frame(master, height = 160, width = 100)
		self.frame1 = Frame(self.bigframe, height = 160, width = 100)
		self.frame2 = Frame(self.bigframe, height = 160, width = 100)
		self.frame3 = Frame(self.bigframe, height = 160, width = 100)
		self.frame4 = Frame(master, height = 160, width = 100)
		self.frame1.pack(side = LEFT)
		self.frame2.pack(side = LEFT)
		self.frame3.pack(side = LEFT)
		self.bigframe.pack(side = TOP)
		self.frame4.pack(side = TOP)
		

		self.entry1 = StringVar()
		self.entry2 = StringVar()
		self.buton = Button(self.frame1, text = "Search", command = self.options, font = 100)
		self.a = Entry(self.frame2, relief = "sunken", textvariable = self.entry1, width = 10)
		self.scrolbar = Scrollbar(self.frame3, width = 0)
		self.lab_bel1 = Listbox(self.frame3, relief = "sunken", yscrollcommand = self.scrolbar.set, height = 10, width = 200)
		self.scrolbar.config( command = self.lab_bel1.yview )
		self.a.pack(padx = 20)
		self.scrolbar.pack(side = RIGHT,  fill="y")
		self.buton.pack(padx = 20)
		self.lab_bel1.pack(padx = 20)
		self.lert1 = Label(self.frame1, font = ("Times 12"), anchor = "w", text = "Composer: ", wraplength = 90)
		self.lert1.pack(pady = 10)
		self.lert2 = Label(self.frame2, font = ("Times 12"), anchor = "w", text = "UnitPrice: ", wraplength = 110)
		self.lert2.pack(pady = 20)
		self.lab_bel1.bind('<<ListboxSelect>>', self.quality)
		self.wha = Button(self.frame4, text = "Change", command = self.DIO, font = 50)
		self.wha.pack(pady = 20)
		self.rest = Entry(self.frame4, relief = "sunken", textvariable = self.entry2)
		self.rest.pack(pady = 5)
		self.result = []
		self.ok = 0
	def options(self):
		"""При нажатті кнопки Search селектить всі пісні 
		в яких є одинакові букви які були записані через Entry"""
		self.lab_bel1.delete(0, END)
		re = self.a.get()
		la = self.c.execute('''SELECT Name, TrackId FROM tracks WHERE Name LIKE ?''', ("%"+re+"%",))
		self.result = la.fetchall()
		print self.result
		for el in self.result:
			self.lab_bel1.insert(END, el[0])
	def quality(self, evt):
		"""Обробник подій вибору лістбокса який 
		виводить на екран ткінтера автора і ціну пісні."""
		w = evt.widget 
		wryyy = int(w.curselection()[0])
		value = w.get(wryyy)
		ok = self.result[wryyy][1]
		self.reee = self.c.execute('''SELECT Composer, UnitPrice FROM tracks WHERE TrackId = ?''', (ok,))
		self.reee = self.reee.fetchall()
		result1 = self.reee
		s = 'Composer: %s' %(result1[0][0],)
		self.lert1.configure(text = s)
		print result1
		e = 'UnitPrice: %s' %(result1[0][1],)
		self.lert2.configure(text = e)
		print result1
	def DIO(self):
		"""Оновлює ціну на пісню завдяки окремим Bottom і Entry через TrackId"""
		wryyy = int(self.lab_bel1.curselection()[0])
		TrackId = self.result[wryyy][1]
		kono = self.c.execute('''UPDATE tracks SET UnitPrice = ? WHERE TrackId = TrackId''', (self.result[0][1],))
		result1 = kono.fetchall()
		s = 'Composer: %s' %(result1[0][1],)
		self.lert1.configure(text = s)
		der = 0
if __name__ == "__main__":
	master = Tk()
	master.resizable(height = False, width = False)
	master.geometry("700x400")
	app = Author(master)
	master.mainloop()