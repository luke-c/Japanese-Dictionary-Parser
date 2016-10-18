import sqlite3

conn = sqlite3.connect('dictionary.db')
print("Opened/created database successfully")

c = conn.cursor()

c.execute('''CREATE TABLE Kanji_Element
            (_ID INTEGER PRIMARY KEY, 
             ENTRY_ID INTEGER,
             VALUE TEXT)''')
print("Created Kanji_Element Table")

c.execute('''CREATE TABLE Reading_Element
            (_ID INTEGER PRIMARY KEY, 
             ENTRY_ID INTEGER,
             VALUE TEXT)''')
print("Created Reading_Element Table")

c.execute('''CREATE TABLE Sense_Element
            (_ID INTEGER PRIMARY KEY, 
             ENTRY_ID INTEGER)''')
print("Created Sense_Element Table")

c.execute('''CREATE TABLE Gloss
            (_ID INTEGER PRIMARY KEY, 
             VALUE TEXT)''')
print("Created Gloss Table")

c.execute('''CREATE TABLE Gloss_Link
            (_ID INTEGER PRIMARY KEY, 
             GLOSS_ID INTEGER,
             SENSE_ID INTEGER,
             FOREIGN KEY(GLOSS_ID) REFERENCES Gloss(_ID),
             FOREIGN KEY(SENSE_ID) REFERENCES Sense_Element(_ID))''')

print("Created Gloss_Link Table")

c.execute('''CREATE TABLE Pos
            (_ID INTEGER PRIMARY KEY, 
             VALUE TEXT)''')
print("Created Pos Table")

c.execute('''CREATE TABLE Pos_Link
            (_ID INTEGER PRIMARY KEY, 
             POS_ID INTEGER,
             SENSE_ID INTEGER,
             FOREIGN KEY(POS_ID) REFERENCES Pos(_ID),
             FOREIGN KEY(SENSE_ID) REFERENCES Sense_Element(_ID))''')

print("Created Pos_Link Table")

c.execute('''CREATE TABLE Priority
            (_ID INTEGER PRIMARY KEY,
             ENTRY_ID INTEGER,
             VALUE TEXT,
             TYPE TEXT CHECK (TYPE = 'Kanji_Element' OR TYPE = 'Reading_Element'))''')
print("Created Priority Table")

conn.commit()
conn.close()