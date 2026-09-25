import sqlite3

conn = sqlite3.connect("sqlite.db")

conn.execute('''
    CREATE TABLE IF NOT EXISTS student (
        st_id INTEGER PRIMARY KEY AUTOINCREMENT,
        st_name VARCHAR(50),
        st_class VARCHAR(10),
        st_email VARCHAR(30)
    )
''')

conn.execute("""
    INSERT INTO student (st_name, st_class, st_email)
    VALUES ('Ujjwal', 'B.Tech 3rd Year', 'ujjwal@gmail.com')
""")

conn.commit()

data = conn.execute("SELECT * FROM student")

for row in data:
    print(row)

conn.close()