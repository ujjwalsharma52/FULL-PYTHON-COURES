import sqlite3

conn = sqlite3.connect("sqlite.db")

# Tables dekhna
tables = conn.execute("""
    SELECT name FROM sqlite_master
    WHERE type='table'
""")

print("Tables:")
for table in tables:
    print(table)

# Student table ka data
data = conn.execute("SELECT * FROM student")

print("\nStudent Data:")
for row in data:
    print(row)

conn.close()