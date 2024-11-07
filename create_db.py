import sqlite3 
def create_db():
    con=sqlite3.connect(database="rms.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS course(cid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,name TEXT,duration TEXT,charge TEXT,description TEXT)")
    con.commit() 

    cur.execute("CREATE TABLE IF NOT EXISTS student(roll TEXT PRIMARY KEY,name TEXT,email TEXT,gender TEXT,dob TEXT,contact TEXT,date TEXT,course TEXT,city TEXT,state TEXT,pin TEXT,address TEXT)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS result(cid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,roll TEXT,name TEXT,course TEXT,mark INTEGER,fullmark TEXT,per TEXT)")
    con.commit()

    con.close()

create_db()

