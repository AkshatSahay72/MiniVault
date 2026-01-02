import sqlite3

class Database:
    
    def __init__(self, db):
        self.db = db
        con = sqlite3.connect(db)
        cur = con.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS notes(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content TEXT,
                created_at TIMESTAMP
            );
        """)
        con.commit()
        con.close()

    def insert_notes(self, txt):
        con = sqlite3.connect(self.db)
        cur = con.cursor()
        cur.execute(
            "INSERT INTO notes(content, created_at) VALUES(?, datetime('now'));",
            (txt,)
        )
        con.commit()
        con.close()

    def get_all_notes(self):
        con = sqlite3.connect(self.db)
        cur = con.cursor()
        stmt = cur.execute("SELECT * FROM notes;")
        rows = stmt.fetchall()
        con.close()
        return rows