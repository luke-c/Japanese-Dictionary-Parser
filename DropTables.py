import sqlite3

conn = sqlite3.connect('dictionary.db')
print("Opened database successfully")

c = conn.cursor()

c.execute('DROP TABLE Kanji_Element')
print("Dropped Kanji_Element Table")

c.execute('DROP TABLE Reading_Element')
print("Dropped Reading_Element Table")

c.execute('''DROP TABLE Sense_Element''')
print("Dropped Sense_Element Table")

c.execute('''DROP TABLE Gloss''')
print("Dropped Gloss Table")

c.execute('''DROP TABLE Gloss_Link''')
print("Dropped Gloss_Link Table")

c.execute('''DROP TABLE Pos''')
print("Dropped Pos Table")

c.execute('''DROP TABLE Pos_Link''')
print("Dropped Pos_Link Table")

c.execute('''DROP TABLE Priority''')
print("Dropped Priority Table")

conn.commit()
conn.close()