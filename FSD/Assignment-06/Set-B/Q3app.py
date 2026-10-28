from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def products():
    products = {
        "Laptop": 50000,
        "Mobile": 20000,
        "Tablet": 30000,
        "Headphones": 5000
    }

    expensive = max(products, key=products.get)

    return render_template('Q3.html',
                           product=expensive,
                           price=products[expensive])

app.run(debug=True)