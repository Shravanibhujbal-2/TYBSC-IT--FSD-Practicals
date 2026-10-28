from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return "Welcome to the Home Page of our College"

@app.route('/student')
def student():
    return "Welcome Student! This page contains student information."

@app.route('/faculty')
def faculty():
    return "Welcome! This page contains faculty information."

app.run(debug=True)