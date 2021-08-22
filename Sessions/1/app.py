from flask import Flask,render_template,request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "Hi!This is my app"

@app.route("/", methods=['GET'])
def index():
    if session.get('username'):
        return render_template("index.html")
    else:
        return render_template("login.html")
@app.route("/login", methods=['POST','GET'])
def intro():
    msg = "Login first"
    if request.method=="POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username.lower() == "junaid" and password=="Myapp":
            session['username'] = "Junaid"
            return render_template("index.html")
        else:
            msg = "Incorrect Usrname and Password"
        return render_template("login.html", msg = msg)
    else:
        return render_template("login.html", msg=msg)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
