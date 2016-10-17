import xml.etree.ElementTree as ET
tree = ET.parse('JMdict_e.xml') # Change to JMdict_e.xml for real testing
root = tree.getroot()

count = 0
# For every entry
for entry in root.findall('entry'): # Change to findAll for real testing
    #print("Entry:", count)
    count += 1
    entryId = entry.find('ent_seq').text
    #print("ent_seq:", entryId)
    
    for k_ele in entry.findall('k_ele'): # For every Kanji Element in an entry
        keb = k_ele.find('keb').text 
        #print("keb:", keb)
        ke_pri = k_ele.findall('ke_pri')

        #for x in ke_pri:
            #print("ke_pri:", x.text) # Later insert

    for r_ele in entry.findall('r_ele'): # For every Reading Element in an entry
        reb = r_ele.find('reb').text
        #print("reb:", reb)
        re_pri = r_ele.findall('re_pri')

        #for x in re_pri:
            #print("re_pri:", x.text) # Later insert

    for sense in entry.findall('sense'): # For every Sense element in an entry
        pos = sense.findall('pos')
        #for x in pos:
            #print("pos:", x.text)

        gloss = sense.findall('gloss')
        #for x in gloss:
            #print("gloss:", x.text)

print("Number of entries parsed:", count)