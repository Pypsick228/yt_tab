import sqlite3 
con = sqlite3.connect("video.db") # соединение с базой данных, если бд нет, то файл создастся

cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS video(ID INTEGER, Name TEXT NOT NULL, Link TEXT NOT NULL, Autor TEXT, Release_date TEXT, Description TEXT)")
cur.execute("""
    INSERT INTO video VALUES
        (123, "Vid", "Ссылка", "Автор", "Дата", "Описание")
""")

con.commit()
for row in cur.execute("SELECT * FROM video"):
    print(row)
con.close()