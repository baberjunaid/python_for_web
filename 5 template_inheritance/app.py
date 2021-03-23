from flask import Flask,render_template,request

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")
@app.route("/intro", methods=['POST', 'GET'])
def intro():
    if request.method == "POST":

        name = request.form.get("name")
        email = request.form.get("email")
        program = request.form.get("program")
        fav = request.form.getlist("fav")
        return render_template("intro.html", name=name, email=email, program=program, fav=fav)
    else:
        return "Kindly go back to <a href='/'> Index</a> page"



if __name__ == "__main__":
    app.run(debug=True)
