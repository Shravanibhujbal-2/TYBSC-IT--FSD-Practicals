from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def employees():
    employees = [
        ["Amit", "IT", 25000],
        ["Priya", "HR", 30000],
        ["Rahul", "Sales", 28000],
        ["Sneha", "Finance", 32000],
        ["Neha", "Marketing", 27000]
    ]

    return render_template('Q1.html', employees=employees)

app.run(debug=True)