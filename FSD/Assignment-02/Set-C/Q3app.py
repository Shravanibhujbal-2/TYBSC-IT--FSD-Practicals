from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def search():

    book = ""

    if request.method == 'POST':
        book = request.form['book']

    return render_template('Q3.html', book=book)

app.run(debug=True)