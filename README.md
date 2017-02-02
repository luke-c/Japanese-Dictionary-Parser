# Japanese-Dictionary-Parser

Run 'CreateTables.py' to create a database with the required tables, the output will be 'dictionary.db' 

Place 'JMdict_e.xml' and 'JMnedict.xml' in the same directory as the Python files, and run 'ParseXmlToSql.py'. This will populate the previously created database.

Run 'DropTables.py' to delete all tables from the database.


Notes:
You can specify the files yourself in 'ParseXmlToSql'. 
Also works fine with the standard larger JMdict file.
