import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "fitbuddy.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users 
                 (id INTEGER PRIMARY KEY, name TEXT, bmi REAL, goal TEXT, date TEXT, feedback TEXT)''')
    conn.commit()
    conn.close()

def save_user(name, bmi, goal, feedback=""):
    import datetime
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO users (name,bmi,goal,date,feedback) VALUES (?,?,?,?,?)", 
              (name, bmi, goal, str(datetime.date.today()), feedback))
    conn.commit()
    conn.close()

def save_feedback(name, feedback):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("UPDATE users SET feedback=? WHERE name=?", (feedback, name))
    conn.commit()
    conn.close()

def get_all_users():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    data = c.fetchall()
    conn.close()
    return data