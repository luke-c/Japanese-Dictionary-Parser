import xml.etree.ElementTree as ET
import sqlite3
import time

tree = ET.parse('JMnedict.xml')
root = tree.getroot()

conn = sqlite3.connect('dictionary.db')
print("Opened database successfully")

c = conn.cursor()

count = 0
start_time = time.time()
print("Starting parsing of JMnedict")

# For every entry
for entry in root.findall('entry'):  # Change to findAll for real testing
    entryId = entry.find('ent_seq').text
    count += 1

    for k_ele in entry.findall('k_ele'):  # For every Kanji Element in an entry
        keb = k_ele.find('keb').text
        c.execute('INSERT INTO Kanji_Element (ENTRY_ID, VALUE) VALUES (?, ?)',
                  (entryId, keb))

        ke_pri = k_ele.findall('ke_pri')
        for priority in ke_pri:
            c.execute('INSERT INTO Priority (ENTRY_ID, VALUE, TYPE) VALUES (?, ?, ?)',
                      (entryId, priority.text, 'Kanji_Element'))

    for r_ele in entry.findall('r_ele'):  # For every Reading Element in an entry
        reb = r_ele.find('reb').text
        c.execute('INSERT INTO Reading_Element (ENTRY_ID, VALUE) VALUES (?, ?)',
                  (entryId, reb))

        re_pri = r_ele.findall('re_pri')
        for priority in re_pri:
            c.execute('INSERT INTO Priority (ENTRY_ID, VALUE, TYPE) VALUES (?, ?, ?)',
                      (entryId, priority.text, 'Reading_Element'))

    for trans in entry.findall('trans'):  # For every Translation Element in an entry
        c.execute('INSERT INTO Sense_Element (ENTRY_ID) VALUES (?)',
                  (entryId,))

        c.execute('SELECT last_insert_rowid()')
        senseId = c.fetchone()[0]

        typeList = trans.findall('name_type')
        for nameType in typeList:
            c.execute('INSERT INTO Pos (VALUE) VALUES (?)',
                      (nameType.text,))

            c.execute('SELECT last_insert_rowid()')
            typeId = c.fetchone()[0]

            c.execute('INSERT INTO Pos_Link (POS_ID, SENSE_ID) VALUES (?, ?)',
                      (typeId, senseId))

        transList = trans.findall('trans_det')
        for transDet in transList:
            c.execute('INSERT INTO Gloss (VALUE) VALUES (?)',
                      (transDet.text,))

            c.execute('SELECT last_insert_rowid()')
            glossId = c.fetchone()[0]

            c.execute('INSERT INTO Gloss_Link (GLOSS_ID, SENSE_ID) VALUES (?, ?)',
                      (glossId, senseId))

conn.commit()
conn.close()

print("Completed parsing of JMnedict")
print("Number of entries parsed:", count)
print("--- %s seconds ---" % (time.time() - start_time))
