from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    conn = sqlite3.connect("projects.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM projects")
    projects = cursor.fetchall()

    conn.close()

    return render_template("index.html", projects=projects)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)