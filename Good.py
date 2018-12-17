import sqlite3
conn = sqlite3.connect('chinook.db')
c = conn.cursor()
query = c.execute('''SELECT * FROM Albums Where ArtistId > 8 and ArtistId < 30''');
for row in query:
	print row
conn.commit()
conn.close()