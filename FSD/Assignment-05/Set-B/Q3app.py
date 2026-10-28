from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def salary():
    basic = ""
    total = ""

    if request.method == 'POST':
        basic = request.form['basic']
        total = float(basic) + 5000

    return render_template('Q3.html', basic=basic, total=total)

app.run(debug=True)