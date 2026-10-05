def get_bmi(weight, height):
    # height cm me aayegi to meter me convert
    if height > 3:
        height = height / 100
    bmi = weight / (height * height)
    return round(bmi, 2)

def get_plan(bmi, goal):
    if goal == 'weight_loss':
        diet = 'Low Carb, High Protein - 1500 calories'
        workout = 'Cardio + HIIT 5 days/week'
    elif goal == 'muscle_gain':
        diet = 'High Protein, High Calorie - 2800 calories'
        workout = 'Weight Training 6 days/week'
    else:
        diet = 'Balanced Diet - 2200 calories'
        workout = 'Mix of Cardio and Strength 4 days/week'

    if bmi < 18.5:
        extra = ' (You are underweight, focus on muscle gain)'
    elif bmi > 25:
        extra = ' (You are overweight, focus on fat loss)'
    else:
        extra = ' (Your BMI is normal)'

    return {'diet': diet + extra, 'workout': workout, 'bmi_status': extra}
