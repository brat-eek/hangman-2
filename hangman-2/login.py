import sqlite3

conn=sqlite3.connect("once.db")
cur=conn.cursor()
print 'IF U WANNA PLAY N KEEP A TRACK OF EFFICIENCY , ENTER UR NAME'
naam=raw_input()
chalja = "INSERT INTO leader_board (name,played,wins) VALUES ('"+ naam +"',0,0)"
cur.execute(chalja)
conn.commit()
conn.close()

