from flask import Flask

app = Flask(__name__)

@app.route('/')
def subjects():
    subjects = ["Python", "Java", "DBMS", "Web Development", "Computer Networks"]
    return "<br>".join(subjects)

app.run(debug=True)