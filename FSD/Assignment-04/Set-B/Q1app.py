from flask import Flask

app = Flask(__name__)

@app.route('/student/<name>')
def student(name):
    return "Welcome " + name + "! You are a student of our college."

app.run(debug=True)