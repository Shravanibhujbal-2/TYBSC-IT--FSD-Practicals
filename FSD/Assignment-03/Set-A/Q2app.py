from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Name: Shravani Bhujbal <br> Roll No:18"

app.run(debug=True)