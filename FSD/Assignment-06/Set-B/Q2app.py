from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def employees():
    employees = [
        {"name": "Amit", "department": "IT"},
        {"name": "Priya", "department": "HR"},
        {"name": "Rahul", "department": "Sales"},
        {"name": "Sneha", "department": "Finance"},
        {"name": "Neha", "department": "Marketing"}
    ]

    return render_template('Q2.html', employees=employees)

app.run(debug=True)