from flask import Flask

app = Flask(__name__)

@app.route('/course/<name>')
def course(name):
    return "Course Name: " + name + "<br>Course Information: This course provides technical and practical knowledge."

app.run(debug=True)