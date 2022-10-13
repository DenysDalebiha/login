from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = '4fDASJ3gu8u9*yt%Re34Ejkl'

menu = [{"name":"home", "url": "index"},
        {"name":"login", "url": "login"}]

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title = "Home", menu=menu)


@app.route("/login", methods=["POST", "GET"])
def login():
    return render_template("login.html", title='login', menu=menu)

@app.route("/<username>")
def profile(username):
    # if 'userLogged' not in session or session['userLogged'] != username:
    #     abort(401)
    if username == 'admin':
        return render_template("admin.html", menu=menu)
    return render_template("user.html", username=username,  menu=menu)

@app.errorhandler(404)
def pageNotFound(error):
    return render_template('page404.html'), 404


if __name__ == "__main__":
    app.run(debug=True)
