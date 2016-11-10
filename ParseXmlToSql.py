import xml.etree.ElementTree as ET
import sqlite3
import time


conn = sqlite3.connect('dictionary.db')
print("Opened database successfully")


def parse_jmdict(xml_file='JMdict_e.xml'):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    c = conn.cursor()
    entries_processed = 0
    start_time = time.time()
    print("Starting parsing of {0}".format(xml_file))

    # For every entry
    for entry in root.findall('entry'):
        entry_id = entry.find('ent_seq').text

        for k_ele in entry.findall('k_ele'):  # For every Kanji Element in an entry
            keb = k_ele.find('keb').text
            c.execute('INSERT INTO Jmdict_Kanji_Element (ENTRY_ID, VALUE) VALUES (?, ?)',
                      (entry_id, keb))

            ke_pri = k_ele.findall('ke_pri')
            for priority in ke_pri:
                c.execute('INSERT INTO Jmdict_Priority (ENTRY_ID, VALUE, TYPE) VALUES (?, ?, ?)',
                          (entry_id, priority.text, 'Kanji_Element'))

        for r_ele in entry.findall('r_ele'):  # For every Reading Element in an entry
            reb = r_ele.find('reb').text
            c.execute('INSERT INTO Jmdict_Reading_Element (ENTRY_ID, VALUE) VALUES (?, ?)',
                      (entry_id, reb))

            c.execute('SELECT last_insert_rowid()')
            r_ele_id = c.fetchone()[0]

            re_restr_list = r_ele.findall('re_restr')
            for re_restr in re_restr_list:
                c.execute('INSERT INTO Jmdict_Reading_Relation (ENTRY_ID, READING_ELEMENT_ID, VALUE) VALUES (?, ?, ?)',
                          (entry_id, r_ele_id, re_restr.text))

            re_pri = r_ele.findall('re_pri')
            for priority in re_pri:
                c.execute('INSERT INTO Jmdict_Priority (ENTRY_ID, VALUE, TYPE) VALUES (?, ?, ?)',
                          (entry_id, priority.text, 'Reading_Element'))

        for sense in entry.findall('sense'):  # For every Sense element in an entry
            c.execute('INSERT INTO Jmdict_Sense_Element (ENTRY_ID) VALUES (?)',
                      (entry_id,))

            c.execute('SELECT last_insert_rowid()')
            sense_id = c.fetchone()[0]

            pos_list = sense.findall('pos')
            for pos in pos_list:
                c.execute('INSERT INTO Jmdict_Pos (VALUE) VALUES (?)',
                          (pos.text,))

                c.execute('SELECT last_insert_rowid()')
                pos_id = c.fetchone()[0]

                c.execute('INSERT INTO Jmdict_Pos_Link (POS_ID, SENSE_ID) VALUES (?, ?)',
                          (pos_id, sense_id))

            gloss_list = sense.findall('gloss')
            for gloss in gloss_list:
                c.execute('INSERT INTO Jmdict_Gloss (ENTRY_ID, VALUE) VALUES (?, ?)',
                          (entry_id, gloss.text))

                c.execute('SELECT last_insert_rowid()')
                gloss_id = c.fetchone()[0]

                c.execute('INSERT INTO Jmdict_Gloss_Link (GLOSS_ID, SENSE_ID) VALUES (?, ?)',
                          (gloss_id, sense_id))

        entries_processed += 1
    conn.commit()
    print("Completed parsing of {0}".format(xml_file))
    print("Number of entries parsed: {0}".format(entries_processed))
    print("--- %s seconds ---" % (time.time() - start_time))


def parse_jmnedict(xml_file = 'JMnedict.xml'):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    c = conn.cursor()
    count = 0
    start_time = time.time()
    print("Starting parsing of {0}".format(xml_file))

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
    print("Completed parsing of JMnedict")
    print("Number of entries parsed:", count)
    print("--- %s seconds ---" % (time.time() - start_time))


parse_jmdict()
#parse_jmnedict()
conn.close()
