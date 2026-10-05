from flask import Flask, render_template, request
from app.ai_logic import get_bmi, get_plan
from app.database import init_db, save_user, get_all_users

app = Flask(_name_, template_folder='templates')
init_db()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        height = float(request.form['height'])
        weight = float(request.form['weight'])
        goal = request.form['goal']
        bmi = get_bmi(weight, height)
        plan = get_plan(bmi, goal)
        save_user(name, bmi, goal)
        return render_template('plan.html', name=name, bmi=bmi, plan=plan)
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    users = get_all_users()
    return render_template('dashboard.html', users=users)

if _name_ == '_main_':
    app.run(debug=True)
