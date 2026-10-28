from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def marks():
    marks = [80, 75, 90, 65, 70]

    total = sum(marks)
    average = total / len(marks)
    highest = max(marks)
    lowest = min(marks)

    return render_template('Q3.html',
                           marks=marks,
                           total=total,
                           average=average,
                           highest=highest,
                           lowest=lowest)

app.run(debug=True)