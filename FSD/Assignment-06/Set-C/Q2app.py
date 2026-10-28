from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def students():
    students = {
        "Shravani": 75,
        "Priya": 55,
        "Rahul": 80,
        "Amit": 45,
        "Sneha": 70
    }

    passed = {name: marks for name, marks in students.items() if marks > 60}

    return render_template('Q2.html', students=passed)

app.run(debug=True)