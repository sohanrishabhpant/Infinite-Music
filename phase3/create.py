import sqlite3

conn = sqlite3.connect('playlist.db')
cursor = conn.cursor()
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS playlist(
    id INTEGER PRIMARY KEY,
    song_name TEXT,
    duration INTEGER
);''')
               
x=9898
y=989989
conn.commit()

conn.close()