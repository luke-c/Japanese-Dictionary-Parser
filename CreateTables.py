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
    c.execute('''CREATE INDEX Jmdict_Kanji_Element_VALUE_Index
            ON Jmdict_Kanji_Element (VALUE)''')

    # Reading Element
    c.execute('''CREATE TABLE Jmdict_Reading_Element
            (_ID INTEGER PRIMARY KEY,
             ENTRY_ID INTEGER NOT NULL,
             VALUE TEXT NOT NULL,
             NO_KANJI INTEGER NOT NULL)''')
    c.execute('''CREATE INDEX Jmdict_Reading_Element_ENTRY_ID_Index
            ON Jmdict_Reading_Element (ENTRY_ID)''')
    c.execute('''CREATE INDEX Jmdict_Reading_Element_VALUE_Index
                ON Jmdict_Reading_Element (VALUE)''')

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

    # Sense Element
    c.execute('''CREATE TABLE Jmdict_Sense_Element
            (_ID INTEGER PRIMARY KEY,
             ENTRY_ID INTEGER NOT NULL)''')
    c.execute('''CREATE INDEX Jmdict_Sense_Element_ENTRY_ID_Index
            ON Jmdict_Sense_Element (ENTRY_ID)''')

    # Gloss
    c.execute('''CREATE TABLE Jmdict_Gloss
            (_ID INTEGER PRIMARY KEY,
             ENTRY_ID INTEGER NOT NULL,
             SENSE_ID INTEGER NOT NULL,
             VALUE TEXT NOT NULL COLLATE NOCASE,
             FOREIGN KEY(SENSE_ID) REFERENCES Jmdict_Sense_Element(_ID))''')
    c.execute('''CREATE INDEX Jmdict_Gloss_ENTRY_ID_Index
            ON Jmdict_Gloss (ENTRY_ID)''')
    c.execute('''CREATE INDEX Jmdict_Gloss_SENSE_ID_Index
            ON Jmdict_Gloss (SENSE_ID)''')
    c.execute('''CREATE INDEX Jmdict_Gloss_VALUE_Index
                ON Jmdict_Gloss (VALUE)''')

    # Pos
    c.execute('''CREATE TABLE Jmdict_Sense_Pos
            (_ID INTEGER PRIMARY KEY,
             SENSE_ID INTEGER NOT NULL,
             VALUE TEXT NOT NULL,
             FOREIGN KEY(SENSE_ID) REFERENCES Jmdict_Sense_Element(_ID))''')
    c.execute('''CREATE INDEX Jmdict_Sense_Pos_SENSE_ID_Index
                ON Jmdict_Sense_Pos (SENSE_ID)''')

    # Field
    c.execute('''CREATE TABLE Jmdict_Sense_Field
                (_ID INTEGER PRIMARY KEY,
                 SENSE_ID INTEGER NOT NULL,
                 VALUE TEXT NOT NULL,
                 FOREIGN KEY(SENSE_ID) REFERENCES Jmdict_Sense_Element(_ID))''')
    c.execute('''CREATE INDEX Jmdict_Sense_Field_SENSE_ID_Index
                    ON Jmdict_Sense_Field (SENSE_ID)''')

    # Dialect
    c.execute('''CREATE TABLE Jmdict_Sense_Dialect
                    (_ID INTEGER PRIMARY KEY,
                     SENSE_ID INTEGER NOT NULL,
                     VALUE TEXT NOT NULL,
                     FOREIGN KEY(SENSE_ID) REFERENCES Jmdict_Sense_Element(_ID))''')
    c.execute('''CREATE INDEX Jmdict_Sense_Dialect_SENSE_ID_Index
                        ON Jmdict_Sense_Dialect (SENSE_ID)''')

    # Priority
    c.execute('''CREATE TABLE Jmdict_Priority
            (_ID INTEGER PRIMARY KEY,
             ENTRY_ID INTEGER NOT NULL,
             VALUE TEXT NOT NULL,
             TYPE TEXT CHECK (TYPE = 'Kanji_Element' OR TYPE = 'Reading_Element'))''')
    c.execute('''CREATE INDEX Jmdict_Priority_ENTRY_ID_Index
            ON Jmdict_Priority (ENTRY_ID)''')

    conn.commit()
    print("Created JMdict Tables")


def create_jmnedict_tables():
    c = conn.cursor()

    # Kanji Element
    c.execute('''CREATE TABLE Jmnedict_Kanji_Element
                (_ID INTEGER PRIMARY KEY,
                 ENTRY_ID INTEGER NOT NULL,
                 VALUE TEXT NOT NULL)''')
    c.execute('''CREATE INDEX Jmnedict_Kanji_Element_ENTRY_ID_Index
                ON Jmnedict_Kanji_Element (ENTRY_ID)''')
    c.execute('''CREATE INDEX Jmnedict_Kanji_Element_VALUE_Index
                    ON Jmnedict_Kanji_Element (VALUE)''')

    # Reading Element
    c.execute('''CREATE TABLE Jmnedict_Reading_Element
                (_ID INTEGER PRIMARY KEY,
                 ENTRY_ID INTEGER NOT NULL,
                 VALUE TEXT NOT NULL)''')
    c.execute('''CREATE INDEX Jmnedict_Reading_Element_ENTRY_ID_Index
                ON Jmnedict_Reading_Element (ENTRY_ID)''')
    c.execute('''CREATE INDEX Jmnedict_Reading_Element_VALUE_Index
                    ON Jmnedict_Reading_Element (VALUE)''')

    # Trans Element
    c.execute('''CREATE TABLE Jmnedict_Trans_Element
                (_ID INTEGER PRIMARY KEY,
                 ENTRY_ID INTEGER NOT NULL)''')
    c.execute('''CREATE INDEX Jmnedict_Trans_Element_ENTRY_ID_Index
                ON Jmnedict_Trans_Element (ENTRY_ID)''')

    # Gloss
    c.execute('''CREATE TABLE Jmnedict_Gloss
            (_ID INTEGER PRIMARY KEY,
             ENTRY_ID INTEGER NOT NULL,
             TRANS_ELEMENT_ID INTEGER NOT NULL,
             VALUE TEXT NOT NULL,
             FOREIGN KEY(TRANS_ELEMENT_ID) REFERENCES Jmnedict_Trans_Element(_ID))''')
    c.execute('''CREATE INDEX Jmnedict_Gloss_ENTRY_ID_Index
            ON Jmnedict_Gloss (ENTRY_ID)''')
    c.execute('''CREATE INDEX Jmnedict_Gloss_TRANS_ELEMENT_ID_Index
            ON Jmnedict_Gloss (TRANS_ELEMENT_ID)''')
    c.execute('''CREATE INDEX Jmnedict_Gloss_VALUE_Index
                    ON Jmnedict_Gloss (VALUE)''')

    # Name Type
    c.execute('''CREATE TABLE Jmnedict_Trans_Name_Type
            (_ID INTEGER PRIMARY KEY,
             TRANS_ELEMENT_ID INTEGER NOT NULL,
             VALUE TEXT NOT NULL,
             FOREIGN KEY(TRANS_ELEMENT_ID) REFERENCES Jmnedict_Trans_Element(_ID))''')
    c.execute('''CREATE INDEX Jmnedict_Trans_Name_Type_TRANS_ELEMENT_ID_Index
                ON Jmnedict_Trans_Name_Type (TRANS_ELEMENT_ID)''')


    conn.commit()
    print("Created JMnedict Tables")


def create_user_tables():
    c = conn.cursor()

    # Favourites
    c.execute('''CREATE TABLE User_Favourites
                    (ENRTY_ID INTEGER PRIMARY KEY NOT NULL)''')


create_jmdict_tables()
#create_jmnedict_tables()
conn.close()
