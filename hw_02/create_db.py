import sqlite3

conn = sqlite3.connect('phones.db')
cur = conn.cursor()

# Create table
cur.execute('''
CREATE TABLE phones
(ContactName varchar(128), phone varchar(128) UNIQUE)
''')

# Save (commit) the changes
conn.commit()

conn.close()


'''
1. Создать таблицу phones с полями contactName, phone
'''