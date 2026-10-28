from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def area():
    length = ""
    breadth = ""
    result = ""

    if request.method == 'POST':
        length = request.form['length']
        breadth = request.form['breadth']
        result = float(length) * float(breadth)

    return render_template('Q3.html',
                           length=length,
                           breadth=breadth,
                           result=result)

app.run(debug=True)