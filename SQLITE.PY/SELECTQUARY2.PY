import sqlite3
conn=sqlite3.connect("sqlite.db")
data=conn.execute("SELECT * FROM student  limit 2,2")# IS ME DATA 2 POSTION SE START HOGA OR 2 DATA SHOW HOGA IS ME 3 OR 5 KA DATA DIKHAYE Q KI 4 DELETE HO GAY HAI
print("STUDENT ID ", "STUDENT NAME ","STUDENT CLASS", "STUDENT EMAIL")
for n in data:
  print(n[0], " " , n[1]," ",n[2], n[3])