from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def student():
    name = "Shravani"
    marks = [80, 75, 90, 85, 70]

    total = sum(marks)
    average = total / len(marks)

    return render_template('Q1.html',
                           name=name,
                           marks=marks,
                           total=total,
                           average=average)

app.run(debug=True)