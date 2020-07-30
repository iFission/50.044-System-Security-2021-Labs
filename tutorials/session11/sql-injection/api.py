from flask import Flask, request, render_template
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)


@app.route("/get")
def get():
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("select * from data")
    data = c.fetchall()
    return "<br>".join([i[0] for i in data])


@app.route("/register")
def register():
    code = request.args.get('code')
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    try:
        c.execute("INSERT INTO data VALUES (?)", (code,))
        conn.commit()
        return "Successfully added {code}"
    except sqlite3.Error as e:
        return str(e)


@app.route("/search")
def search():
    code = request.args.get('code')
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    try:
        statement = "select * from data where data='" + code + "'"
        c.execute(statement)
        found = c.fetchall()
        if found == []:
            return "Invalid Code<br>{statement}"
        else:
            return "Wifi Connection Established<br>{statement}"
    except sqlite3.Error as e:
        return str(e) + "<br>{statement}"


@app.route("/login")
def login():
    return open("login.html").read()


@app.route("/submit.js")
def submit():
    return open("submit.js").read()


@app.route("/")
def main():
    return open("403.html").read()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
