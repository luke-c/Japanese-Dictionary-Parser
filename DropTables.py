import sqlite3

conn = sqlite3.connect('dictionary.db')
print("Opened database successfully")


def drop_jmdict_tables():
    c = conn.cursor()
    c.execute('''DROP TABLE Jmdict_Kanji_Element''')
    c.execute('''DROP TABLE Jmdict_Reading_Element''')
    c.execute('''DROP TABLE Jmdict_Reading_Relation''')
    c.execute('''DROP TABLE Jmdict_Sense_Element''')
    c.execute('''DROP TABLE Jmdict_Gloss''')
    c.execute('''DROP TABLE Jmdict_Sense_Pos''')
    c.execute('''DROP TABLE Jmdict_Sense_Field''')
    c.execute('''DROP TABLE Jmdict_Sense_Dialect''')
    c.execute('''DROP TABLE Jmdict_Priority''')
    conn.commit()
    print("Dropped Jmdict Tables")


def drop_jmnedict_tables():
    c = conn.cursor()
    c.execute('''DROP TABLE Jmnedict_Kanji_Element''')
    c.execute('''DROP TABLE Jmnedict_Reading_Element''')
    c.execute('''DROP TABLE Jmnedict_Trans_Element''')
    c.execute('''DROP TABLE Jmnedict_Gloss''')
    c.execute('''DROP TABLE Jmnedict_Trans_Name_Type''')
    conn.commit()
    print("Dropped Jmnedict Tables")


def drop_user_tables():
    c = conn.cursor()
    c.execute('''DROP TABLE User_Favourites''')
    conn.commit()
    print("Dropped User Tables")


drop_jmdict_tables()
#drop_jmnedict_tables()
drop_user_tables()
conn.close()
