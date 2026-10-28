from flask import Flask
from datetime import date

app = Flask(__name__)

@app.route('/')
def home():
    return str(date.today())

app.run(debug=True)