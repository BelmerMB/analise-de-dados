import sqlite3

dc = sqlite3.connect('test.db')
qry="DELETE from material where name=?"
nm = 'Abbas'
try:
    cur=dc.cursor()
    cur.execute(qry, (nm,))
    dc.commit()
    print("record deleted")
except:
    print('fail')
    dc.rollback()
dc.close()