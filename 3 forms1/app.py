from flask import Flask,render_template,request

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")
@app.route("/intro", methods=['POST'])
def intro():
    fname = request.form.get("fname")
    lname = request.form.get("lname")
    program = request.form.get("program")
    return "Hello " + str(fname) + " " +  str(lname) +" from " + program




if __name__ == "__main__":
    app.run(debug=True)
