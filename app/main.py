from flask import Flask, render_template, request
from ai_logic import get_bmi, get_plan
import os
import sqlite3

app = Flask(__name__, template_folder='../templates', static_folder='../static')

os.makedirs('data', exist_ok=True)
conn = sqlite3.connect('data/fitbuddy.db')
conn.execute('''CREATE TABLE IF NOT EXISTS users 
(name TEXT, age INT, gender TEXT, height REAL, weight REAL, goal TEXT, activity TEXT, diet TEXT, health TEXT, days INT)''')
conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        gender = request.form.get('gender')
        height = float(request.form.get('height'))
        weight = float(request.form.get('weight'))
        goal = request.form.get('goal')
        activity = request.form.get('activity')
        diet = request.form.get('diet')
        health = request.form.get('health')
        days = request.form.get('days')
        bmi = get_bmi(weight, height)
        plan = get_plan(bmi, goal, activity, diet, health, days, gender, age)
        con = sqlite3.connect('data/fitbuddy.db')
        con.execute("INSERT INTO users VALUES (?,?,?,?,?,?,?,?,?,?)",
                    (name, age, gender, height, weight, goal, activity, diet, health, days))
        con.commit()
        con.close()
        user_obj = {"name": name, "age": age, "gender": gender, "goal": goal}
        return render_template('plan.html', user=user_obj, name=name, gender=gender, goal=goal, activity=activity, diet=diet, health=health, days=days, bmi=round(bmi,1), plan=plan)
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    con = sqlite3.connect('data/fitbuddy.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM users ORDER BY rowid DESC")
    users = cur.fetchall()
    con.close()
    return render_template('dashboard.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)