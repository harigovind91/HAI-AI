import sqlite3

def init_db():
    conn = sqlite3.connect('hai_global.db')
    c = conn.cursor()
    # यूजर और प्रोजेक्ट्स टेबल
    c.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS projects (id INTEGER PRIMARY KEY, user_id INTEGER, name TEXT, code TEXT)')
    # वैकेंसी टेबल
    c.execute('CREATE TABLE IF NOT EXISTS vacancy (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, skill TEXT, status TEXT DEFAULT "Pending")')
    conn.commit()
    conn.close()
    print("Database Initialized Successfully!")

if __name__ == "__main__":
    init_db()
  
