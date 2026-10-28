from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def home():
    conn = psycopg2.connect(
        host="localhost",
        database="student",
        user="postgres",
        password="root"
    )

    conn.close()

    return "Database Connected Successfully"

if __name__ == '__main__':
    app.run(debug=True)