import sqlite3
db=sqlite3.connect('test.db')
qry="insert into material (name, age, marks) values('elmer', 20, 80);"

try:
    cur=db.cursor()
    cur.execute(qry)
    db.commit()
    print ("record added successfully")

except:
    print ("error in query")
    db.rollback()
db.close()