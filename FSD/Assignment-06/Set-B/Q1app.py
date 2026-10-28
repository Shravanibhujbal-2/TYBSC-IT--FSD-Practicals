from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def student():
    student = {
        "Name": "Shravani",
        "Roll No": 101,
        "Class": "TYBSc IT"
    }
    return render_template('Q1.html', student=student)

app.run(debug=True)