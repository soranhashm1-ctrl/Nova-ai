import sqlite3

def init_db():
    conn = sqlite3.connect("novaai.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS chats (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        chat_id INTEGER,
        role TEXT,
        content TEXT
    )
    """)

    conn.commit()
    conn.close()

def create_chat(title):
    conn = sqlite3.connect("novaai.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO chats (title) VALUES (?)",
        (title,)
    )

    chat_id = cursor.lastrowid
    conn.commit()
    conn.close()

    return chat_id
