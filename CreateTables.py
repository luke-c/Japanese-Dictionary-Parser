import sqlite3

conn = sqlite3.connect('dictionary.db')
print("Opened/created database successfully")

c = conn.cursor()

# Kanji Element
c.execute('''CREATE TABLE Kanji_Element
            (_ID INTEGER PRIMARY KEY, 
             ENTRY_ID INTEGER NOT NULL,
             VALUE TEXT NOT NULL)''')

c.execute('''CREATE INDEX Kanji_Element_ENTRY_ID_Index
            ON Kanji_Element (ENTRY_ID)''')

print("Created Kanji_Element Table")

# Reading Element
c.execute('''CREATE TABLE Reading_Element
            (_ID INTEGER PRIMARY KEY, 
             ENTRY_ID INTEGER NOT NULL,
             VALUE TEXT NOT NULL)''')

c.execute('''CREATE INDEX Reading_Element_ENTRY_ID_Index
            ON Reading_Element (ENTRY_ID)''')

print("Created Reading_Element Table")

# Sense Element
c.execute('''CREATE TABLE Sense_Element
            (_ID INTEGER PRIMARY KEY, 
             ENTRY_ID INTEGER NOT NULL)''')

c.execute('''CREATE INDEX Sense_Element_ENTRY_ID_Index
            ON Sense_Element (ENTRY_ID)''')

print("Created Sense_Element Table")

# Gloss
c.execute('''CREATE TABLE Gloss
            (_ID INTEGER PRIMARY KEY, 
             VALUE TEXT NOT NULL)''')

print("Created Gloss Table")

# Gloss Link
c.execute('''CREATE TABLE Gloss_Link
            (_ID INTEGER PRIMARY KEY, 
             GLOSS_ID INTEGER NOT NULL,
             SENSE_ID INTEGER NOT NULL,
             FOREIGN KEY(GLOSS_ID) REFERENCES Gloss(_ID),
             FOREIGN KEY(SENSE_ID) REFERENCES Sense_Element(_ID))''')

c.execute('''CREATE INDEX Gloss_Link_GLOSS_ID_Index
            ON Gloss_Link (GLOSS_ID)''')

c.execute('''CREATE INDEX Gloss_Link_SENSE_ID_Index
            ON Gloss_Link (SENSE_ID)''')

print("Created Gloss_Link Table")

# Pos
c.execute('''CREATE TABLE Pos
            (_ID INTEGER PRIMARY KEY, 
             VALUE TEXT NOT NULL)''')

print("Created Pos Table")

# Pos Link
c.execute('''CREATE TABLE Pos_Link
            (_ID INTEGER PRIMARY KEY, 
             POS_ID INTEGER NOT NULL,
             SENSE_ID INTEGER NOT NULL,
             FOREIGN KEY(POS_ID) REFERENCES Pos(_ID),
             FOREIGN KEY(SENSE_ID) REFERENCES Sense_Element(_ID))''')

c.execute('''CREATE INDEX Pos_Link_POS_ID_Index
            ON Pos_Link (POS_ID)''')

c.execute('''CREATE INDEX Pos_Link_SENSE_ID_Index
            ON Pos_Link (SENSE_ID)''')

print("Created Pos_Link Table")

# Priority
c.execute('''CREATE TABLE Priority
            (_ID INTEGER PRIMARY KEY,
             ENTRY_ID INTEGER NOT NULL,
             VALUE TEXT NOT NULL,
             TYPE TEXT CHECK (TYPE = 'Kanji_Element' OR TYPE = 'Reading_Element'))''')

c.execute('''CREATE INDEX Priority_ENTRY_ID_Index
            ON Priority (ENTRY_ID)''')

print("Created Priority Table")

conn.commit()
conn.close()