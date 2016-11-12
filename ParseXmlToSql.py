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
            re_nokanji = r_ele.find('re_nokanji')
            re_nokanji_value = 0
            if re_nokanji is not None:
                re_nokanji_value = 1
            c.execute('INSERT INTO Jmdict_Reading_Element (ENTRY_ID, VALUE, NO_KANJI) VALUES (?, ?, ?)',
                          (entry_id, reb, re_nokanji_value))

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
                c.execute('INSERT INTO Jmdict_Sense_Pos (SENSE_ID, VALUE) VALUES (?, ?)',
                          (sense_id, pos.text))

            gloss_list = sense.findall('gloss')
            for gloss in gloss_list:
                c.execute('INSERT INTO Jmdict_Gloss (ENTRY_ID, SENSE_ID, VALUE) VALUES (?, ?, ?)',
                          (entry_id, sense_id, gloss.text))

            field_list = sense.findall('field')
            for field in field_list:
                c.execute('INSERT INTO Jmdict_Sense_Field (SENSE_ID, VALUE) VALUES (?, ?)',
                          (sense_id, field.text))

            dialect_list = sense.findall('dial')
            for dial in dialect_list:
                c.execute('INSERT INTO Jmdict_Sense_Dialect (SENSE_ID, VALUE) VALUES (?, ?)',
                          (sense_id, dial.text))

        entries_processed += 1
    conn.commit()
    print("Completed parsing of {0}".format(xml_file))
    print("Number of entries parsed: {0}".format(entries_processed))
    print("--- %s seconds ---" % (time.time() - start_time))


def parse_jmnedict(xml_file = 'JMnedict.xml'):
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
            c.execute('INSERT INTO Jmnedict_Kanji_Element (ENTRY_ID, VALUE) VALUES (?, ?)',
                      (entry_id, keb))

            ke_pri = k_ele.findall('ke_pri')
            for priority in ke_pri:
                c.execute('INSERT INTO Jmnedict_Priority (ENTRY_ID, VALUE, TYPE) VALUES (?, ?, ?)',
                          (entry_id, priority.text, 'Kanji_Element'))

        for r_ele in entry.findall('r_ele'):  # For every Reading Element in an entry
            reb = r_ele.find('reb').text
            c.execute('INSERT INTO Jmnedict_Reading_Element (ENTRY_ID, VALUE) VALUES (?, ?)',
                      (entry_id, reb))

            c.execute('SELECT last_insert_rowid()')
            r_ele_id = c.fetchone()[0]

            re_restr_list = r_ele.findall('re_restr')
            for re_restr in re_restr_list:
                c.execute('INSERT INTO Jmnedict_Reading_Relation (ENTRY_ID, READING_ELEMENT_ID, VALUE) VALUES (?, ?, ?)',
                          (entry_id, r_ele_id, re_restr.text))

            re_pri = r_ele.findall('re_pri')
            for priority in re_pri:
                c.execute('INSERT INTO Jmnedict_Priority (ENTRY_ID, VALUE, TYPE) VALUES (?, ?, ?)',
                          (entry_id, priority.text, 'Reading_Element'))

        for trans in entry.findall('trans'):  # For every Sense element in an entry
            c.execute('INSERT INTO Jmnedict_Trans_Element (ENTRY_ID) VALUES (?)',
                      (entry_id,))

            c.execute('SELECT last_insert_rowid()')
            trans_id = c.fetchone()[0]

            name_type_list = trans.findall('name_type')
            for name_type in name_type_list:
                c.execute('INSERT INTO Jmnedict_Trans_Name_Type (TRANS_ELEMENT_ID, VALUE) VALUES (?, ?)',
                          (trans_id, name_type.text))

            gloss_list = trans.findall('trans_det')
            for gloss in gloss_list:
                c.execute('INSERT INTO Jmnedict_Gloss (ENTRY_ID, TRANS_ELEMENT_ID, VALUE) VALUES (?, ?, ?)',
                          (entry_id, trans_id, gloss.text))

        entries_processed += 1
    conn.commit()
    print("Completed parsing of {0}".format(xml_file))
    print("Number of entries parsed: {0}".format(entries_processed))
    print("--- %s seconds ---" % (time.time() - start_time))


parse_jmdict()
parse_jmnedict()
conn.close()
