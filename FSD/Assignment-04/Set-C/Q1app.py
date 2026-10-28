from flask import Flask

app = Flask(__name__)

@app.route('/product/<int:id>')
def product(id):
    return "Product ID: " + str(id) + "<br>Product Details: This is a useful product."

app.run(debug=True)