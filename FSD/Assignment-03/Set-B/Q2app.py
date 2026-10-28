from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return "Happy Birthday..! <br> Today's date is " + str(datetime.now().date())

app.run(debug=True)