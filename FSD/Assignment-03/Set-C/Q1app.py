from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """ Samarth College of Computer Science offers education in Information Technology.
The Department of Information Technology focuses on programming and technical skills.
Students learn programming, web development, databases and new technologies.
The department encourages practical learning and problem-solving skills."""

app.run(debug=True)