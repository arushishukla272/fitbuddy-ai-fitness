def get_bmi(weight, height_cm):
    height_m = height_cm / 100
    return weight / (height_m * height_m)

def get_plan(bmi, goal, activity="Sedentary", diet="Veg", health="None", days="5", gender="Other", age="25"):
    
    # BMI ke hisab se status
    if bmi < 18.5:
        bmi_status = "Underweight"
    elif bmi < 25:
        bmi_status = "Normal"
    else:
        bmi_status = "Overweight"

    # Plan banao
    plan_text = f"""
    Hello! Your BMI is {round(bmi, 1)} ({bmi_status}).
    
    Goal: {goal}
    Activity: {activity}
    Diet: {diet}
    Health Issue: {health}
    Gender: {gender}, Age: {age}
    Workout: {days} days/week

    DIET PLAN ({diet}):
    - Morning: Warm water + Poha / Oats
    - Lunch: Dal, Roti, Sabzi, Curd
    - Evening: Fruits / Green Tea
    - Dinner: Light khana

    WORKOUT PLAN ({days} days):
    - {days} din workout, walk + bodyweight exercise
    - Activity Level {activity} ke hisab se roz 30 min extra walk

    Note: Health issue {health} ka dhyan rakha gaya hai.
    """
    
    return plan_text