import sqlite3
import os
from flask import Flask, flash, render_template, request, g
import fdatabase as fdb

DATABASE = 'tmp/flsite.db'
DEBUG = True
SECRET_KEY = '4fDASJ3gu8u9*yt%Re34Ejkl'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsite.db')))


def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'], check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


with connect_db() as db:
    dbase = fdb.FDataBase(db)


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.route("/")
def index():
    return render_template("index.html", menu=dbase.getMenu())


@app.route("/login", methods=['POST', "GET"])
def login():
    if request.method == "POST":
        print(request.form.get('username'))
        fdb.Users
        flash("Successful")

    return render_template("/login.html", menu=dbase.getMenu())

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


if __name__ == "__main__":
    app.run(debug=True)