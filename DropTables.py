import sqlite3

conn = sqlite3.connect('dictionary.db')
print("Opened database successfully")


def drop_jmdict_tables():
    c = conn.cursor()
    c.execute('''DROP TABLE Jmdict_Kanji_Element''')
    print("Dropped Jmdict_Kanji_Element Table")
    c.execute('''DROP TABLE Jmdict_Reading_Element''')
    print("Dropped Jmdict_Reading_Element Table")
    c.execute('''DROP TABLE Jmdict_Sense_Element''')
    print("Dropped Jmdict_Sense_Element Table")
    c.execute('''DROP TABLE Jmdict_Gloss''')
    print("Dropped Jmdict_Gloss Table")
    c.execute('''DROP TABLE Jmdict_Gloss_Link''')
    print("Dropped Jmdict_Gloss_Link Table")
    c.execute('''DROP TABLE Jmdict_Pos''')
    print("Dropped Jmdict_Pos Table")
    c.execute('''DROP TABLE Jmdict_Pos_Link''')
    print("Dropped Jmdict_Pos_Link Table")
    c.execute('''DROP TABLE Jmdict_Priority''')
    print("Dropped Jmdict_Priority Table")
    c.execute('''DROP TABLE Jmdict_Reading_Relation''')
    print("Dropped Jmdict_Reading_Relation")
    conn.commit()


drop_jmdict_tables()
conn.close()