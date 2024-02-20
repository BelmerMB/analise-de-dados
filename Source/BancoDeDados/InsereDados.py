import sqlite3
db=sqlite3.connect('test.db')

name = input("digite seu nome: ")

while True:  
    try:
        idade = int(input("Digite sua idade "))
        break
    except:
        print('entre com um numero inteiro')
        continue

while True:
    try:
        valor = float(input("digite um valor: "))
        break
    except:
        print("Entre com um valor real ex: 2.0")
        continue

qry='insert into material (name, age, marks) values(?, ?, ?);'

try:
    cur=db.cursor()
    cur.execute(qry, (name, idade, valor))
    db.commit()
    print ("record added successfully")

except:
    print ("error in query")
    db.rollback()
db.close()