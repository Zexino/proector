import sqlite3
conn = sqlite3.connect('chinook.db')
c = conn.cursor()
query = c.execute('''SELECT * FROM genres;''')
for row in query:
	print row
conn.close()
conn.commit()