from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def result():
    marks = ""
    status = ""

    if request.method == 'POST':
        marks = request.form['marks']

        if int(marks) >= 40:
            status = "Pass"
        else:
            status = "Fail"

    return render_template('Q4.html', marks=marks, status=status)

app.run(debug=True)