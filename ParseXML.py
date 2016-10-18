import xml.etree.ElementTree as ET
import sqlite3
import time

tree = ET.parse('JMdict_e.xml') # Change to JMdict_e.xml for real testing
root = tree.getroot()

conn = sqlite3.connect('dictionary.db')
print("Opened database successfully")

c = conn.cursor()

count = 0
start_time = time.time()
# For every entry
for entry in root.findall('entry'): # Change to findAll for real testing
    entryId = entry.find('ent_seq').text
    count += 1

    for k_ele in entry.findall('k_ele'): # For every Kanji Element in an entry
        keb = k_ele.find('keb').text 
        c.execute('INSERT INTO Kanji_Element (ENTRY_ID, VALUE) VALUES (?, ?)',
                  (entryId, keb))

        ke_pri = k_ele.findall('ke_pri')
        for priority in ke_pri:
            c.execute('INSERT INTO Priority (ENTRY_ID, VALUE, TYPE) VALUES (?, ?, ?)',
                      (entryId, priority.text, 'Kanji_Element'))

    for r_ele in entry.findall('r_ele'): # For every Reading Element in an entry
        reb = r_ele.find('reb').text
        c.execute('INSERT INTO Reading_Element (ENTRY_ID, VALUE) VALUES (?, ?)',
                  (entryId, reb))

        re_pri = r_ele.findall('re_pri')
        for priority in re_pri:
            c.execute('INSERT INTO Priority (ENTRY_ID, VALUE, TYPE) VALUES (?, ?, ?)',
                      (entryId, priority.text, 'Reading_Element'))

    for sense in entry.findall('sense'): # For every Sense element in an entry
        c.execute('INSERT INTO Sense_Element (ENTRY_ID) VALUES (?)',
                  (entryId,))

        c.execute('SELECT last_insert_rowid()')
        senseId = c.fetchone()[0]

        posList = sense.findall('pos')
        for pos in posList:
            c.execute('INSERT INTO Pos (VALUE) VALUES (?)',
                      (pos.text,))

            c.execute('SELECT last_insert_rowid()')
            posId = c.fetchone()[0]

            c.execute('INSERT INTO Pos_Link (POS_ID, SENSE_ID) VALUES (?, ?)',
                      (posId, senseId))

        glossList = sense.findall('gloss')
        for gloss in glossList:
            c.execute('INSERT INTO Gloss (VALUE) VALUES (?)',
                      (gloss.text,))

            c.execute('SELECT last_insert_rowid()')
            glossId = c.fetchone()[0]

            c.execute('INSERT INTO Gloss_Link (GLOSS_ID, SENSE_ID) VALUES (?, ?)',
                      (glossId, senseId))

conn.commit()
conn.close()

print("Number of entries parsed:", count)
print("--- %s seconds ---" % (time.time() - start_time))