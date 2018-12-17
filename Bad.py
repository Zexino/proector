import sqlite3
conn = sqlite3.connect('chinook.db')
c = conn.cursor()
querty = c.execute('''SELECT * FROM tracks WHERE Composer IN('AC/DC','Roy Z')''');
for row in querty:
	print row
conn.commit()
conn.close()