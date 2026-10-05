import sqlite3
import os

def save_user(name, age, weight, height, bmi, goal, activity="Sedentary", diet="Veg", health="None", days="5"):
    try:
        db_path = os.path.join(os.path.dirname(__file__), 'fitbuddy.db')
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        
        # Table banao agar nahi hai toh
        c.execute('''CREATE TABLE IF NOT EXISTS users 
                     (name TEXT, age TEXT, weight REAL, height REAL, bmi REAL, goal TEXT, activity TEXT, diet TEXT, health TEXT, days TEXT)''')
        
        # Data daalo
        c.execute("INSERT INTO users VALUES (?,?,?,?,?,?,?,?,?,?)", 
                  (name, age, weight, height, bmi, goal, activity, diet, health, days))
        
        conn.commit()
        conn.close()
        print("User saved!")
    except Exception as e:
        print(f"DB Error: {e}")