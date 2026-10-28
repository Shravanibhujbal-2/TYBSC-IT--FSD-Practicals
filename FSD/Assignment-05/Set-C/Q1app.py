from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    username = ""
    message = ""

    if request.method == 'POST':
        username = request.form['username']

        if username == "admin":
            message = "Valid Username"
        else:
            message = "Invalid Username"

    return render_template('Q1.html',
                           username=username,
                           message=message)

app.run(debug=True)