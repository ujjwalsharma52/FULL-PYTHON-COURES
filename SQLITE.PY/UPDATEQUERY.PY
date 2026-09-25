import sqlite3
conn=sqlite3.connect("sqlite.db")
conn.execute('''
       update student set st_name='amanlaxmi' ,st_class='MBBS' where st_id=1
             
             
        ''')
conn.commit()
conn.close()