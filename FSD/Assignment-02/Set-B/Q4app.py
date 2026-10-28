from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'admin' and password == '1234':
            return "Login Successful"
        else:
            return "Invalid Login"

    return render_template('Q4.html')

app.run(debug=True)