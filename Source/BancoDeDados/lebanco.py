import sqlite3

db = sqlite3.connect('test.db')

sql = "SELECT * from material"
cursor=db.cursor()
cursor.execute(sql)
while True:
    record=cursor.fetchone()
    if record==None:
        break
    print(record)
db.close()