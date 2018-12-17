import sqlite3
b = sqlite3.connect('example.db')
import csv
with open("sale1.csv","r") as f:
	are = csv.reader(f, delimiter=',', quotechar='|')
	a = b.cursor()
	a.execute('''CREATE TABLE IF NOT EXISTS red
	(date text, trans text, symbol text, qty real, price real)''')
	for row in are:
		a.execute("INSERT INTO red VALUES (?,?,?,?,?)", row)
for row in a.execute('SELECT * FROM red ORDER BY price'):
	print row
b.commit()
b.close()