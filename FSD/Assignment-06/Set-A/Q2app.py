from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def students():
    names = ["Shravani", "Priya", "Rahul", "Amit", "Sneha"]

    return render_template('Q2.html', names=names)

app.run(debug=True)