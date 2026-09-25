import sqlite3
conn=sqlite3.connect("sqlite.db")
data=conn.execute("SELECT * FROM student limit 0,3")# limit mean kon sa data dekhe na hai jise av 0 ,  or 3 hai mean data star hoga 1  matlb 1 postion se data star hoga se show hoga or 3 data  dikhayega
print("STUDENT ID ", "STUDENT NAME ","STUDENT CLASS", "STUDENT EMAIL")
for n in data:
  print(n[0], " " , n[1]," ",n[2], n[3])