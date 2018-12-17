import sqlite3
con = sqlite3.connect('example.db')
c = con.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS stocs (name TEXT NOT NULL, data REAL, surname TEXT NOT NULL)''')
c.execute("INSERT INTO stocs VALUES ('Ted','2015','Green')")
for row in c.execute('SELECT * FROM stocs'):
	print row
con.commit()
con.close()