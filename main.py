from flask import abort, Flask, render_template, redirect, request, session, url_for

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
    if 'userLogged' in session:
        return redirect(url_for("profile", username=session['userLogged']))
    elif request.method == 'POST' and request.form['username'] == "admin" and request.form['pwd'] == '12345':
        session['userLogged'] = request.form['username']
        return redirect(url_for("profile", username=session['userLogged']))
    return render_template("login.html", title='login')

@app.route("/<username>")
def profile(username):
    if 'userLogged' not in session or session['userLogged'] != username:
        abort(401)
    return "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaadmin"

@app.errorhandler(404)
def pageNotFound(error):
    return render_template('page404.html'), 404


if __name__ == "__main__":
    app.run(debug=True)
