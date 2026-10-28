from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def order():
    product = ""
    quantity = ""
    price = ""
    total = ""

    if request.method == 'POST':
        product = request.form['product']
        quantity = request.form['quantity']
        price = request.form['price']
        total = int(quantity) * float(price)

    return render_template('Q2.html',
                           product=product,
                           quantity=quantity,
                           price=price,
                           total=total)

app.run(debug=True)