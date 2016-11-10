import sqlite3

conn = sqlite3.connect('dictionary.db')
print("Opened/created database successfully")


def create_jmdict_tables():
    c = conn.cursor()

    # Kanji Element
    c.execute('''CREATE TABLE Jmdict_Kanji_Element
            (_ID INTEGER PRIMARY KEY,
             ENTRY_ID INTEGER NOT NULL,
             VALUE TEXT NOT NULL)''')
    c.execute('''CREATE INDEX Jmdict_Kanji_Element_ENTRY_ID_Index
            ON Jmdict_Kanji_Element (ENTRY_ID)''')
    print("Created Jmdict_Kanji_Element Table")

    # Reading Element
    c.execute('''CREATE TABLE Jmdict_Reading_Element
            (_ID INTEGER PRIMARY KEY,
             ENTRY_ID INTEGER NOT NULL,
             VALUE TEXT NOT NULL)''')
    c.execute('''CREATE INDEX Jmdict_Reading_Element_ENTRY_ID_Index
            ON Jmdict_Reading_Element (ENTRY_ID)''')
    print("Created Jmdict_Reading_Element Table")

    # Sense Element
    c.execute('''CREATE TABLE Jmdict_Sense_Element
            (_ID INTEGER PRIMARY KEY,
             ENTRY_ID INTEGER NOT NULL)''')
    c.execute('''CREATE INDEX Jmdict_Sense_Element_ENTRY_ID_Index
            ON Jmdict_Sense_Element (ENTRY_ID)''')
    print("Created Jmdict_Sense_Element Table")

    # Gloss
    c.execute('''CREATE TABLE Jmdict_Gloss
            (_ID INTEGER PRIMARY KEY,
             ENTRY_ID INTEGER NOT NULL,
             VALUE TEXT NOT NULL)''')
    c.execute('''CREATE INDEX Jmdict_Gloss_ENTRY_ID_Index
            ON Jmdict_Gloss (ENTRY_ID)''')
    print("Created Jmdict_Gloss Table")

    # Gloss Link
    c.execute('''CREATE TABLE Jmdict_Gloss_Link
            (_ID INTEGER PRIMARY KEY,
             GLOSS_ID INTEGER NOT NULL,
             SENSE_ID INTEGER NOT NULL,
             FOREIGN KEY(GLOSS_ID) REFERENCES Jmdict_Gloss(_ID),
             FOREIGN KEY(SENSE_ID) REFERENCES Jmdict_Sense_Element(_ID))''')
    c.execute('''CREATE INDEX Jmdict_Gloss_Link_GLOSS_ID_Index
            ON Jmdict_Gloss_Link (GLOSS_ID)''')
    c.execute('''CREATE INDEX Jmdict_Gloss_Link_SENSE_ID_Index
            ON Jmdict_Gloss_Link (SENSE_ID)''')
    print("Created Jmdict_Gloss_Link Table")

    # Pos
    c.execute('''CREATE TABLE Jmdict_Pos
            (_ID INTEGER PRIMARY KEY,
             VALUE TEXT NOT NULL)''')
    print("Created Jmdict_Pos Table")

    # Pos Link
    c.execute('''CREATE TABLE Jmdict_Pos_Link
            (_ID INTEGER PRIMARY KEY,
             POS_ID INTEGER NOT NULL,
             SENSE_ID INTEGER NOT NULL,
             FOREIGN KEY(POS_ID) REFERENCES Jmdict_Pos(_ID),
             FOREIGN KEY(SENSE_ID) REFERENCES Jmdict_Sense_Element(_ID))''')
    c.execute('''CREATE INDEX Jmdict_Pos_Link_POS_ID_Index
            ON Jmdict_Pos_Link (POS_ID)''')
    c.execute('''CREATE INDEX Jmdict_Pos_Link_SENSE_ID_Index
            ON Jmdict_Pos_Link (SENSE_ID)''')
    print("Created Jmdict_Pos_Link Table")

    # Priority
    c.execute('''CREATE TABLE Jmdict_Priority
            (_ID INTEGER PRIMARY KEY,
             ENTRY_ID INTEGER NOT NULL,
             VALUE TEXT NOT NULL,
             TYPE TEXT CHECK (TYPE = 'Kanji_Element' OR TYPE = 'Reading_Element'))''')
    c.execute('''CREATE INDEX Jmdict_Priority_ENTRY_ID_Index
            ON Jmdict_Priority (ENTRY_ID)''')
    print("Created Jmdict_Priority Table")

    # Reading Relation
    c.execute('''CREATE TABLE Jmdict_Reading_Relation
            (_ID INTEGER PRIMARY KEY,
             ENTRY_ID INTEGER NOT NULL,
             READING_ELEMENT_ID INTEGER NOT NULL,
             VALUE TEXT NOT NULL,
             FOREIGN KEY(READING_ELEMENT_ID) REFERENCES Jmdict_Reading_Element(_ID))''')
    c.execute('''CREATE INDEX Jmdict_Reading_Relation_ENTRY_ID_Index
            ON Jmdict_Reading_Relation (ENTRY_ID)''')
    c.execute('''CREATE INDEX Jmdict_Reading_Relation_READING_ELEMENT_ID_Index
            ON Jmdict_Reading_Relation (READING_ELEMENT_ID)''')
    conn.commit()


create_jmdict_tables()
conn.close()
