import sqlite3


conn=sqlite3.connect("once.db")
cur=conn.cursor()

cur.execute("CREATE TABLE leader_board (id int IDENTITY(1,1)," \
 "name varchar(20),played int,wins int,PRIMARY KEY (id))")
conn.commit()
conn.close()



