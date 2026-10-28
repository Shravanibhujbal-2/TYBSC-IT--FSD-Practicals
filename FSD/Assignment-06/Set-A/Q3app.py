from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def students():
    names = ["Shravani", "Trupti", "Rachana", "Aditi", "Krupa"]

    names = sorted(names)

    return render_template('Q3.html', names=names)

app.run(debug=True)