from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    name = "John Smith"
    
    loop_iter = 3
    return render_template("index.html", name=name, loop_iter = loop_iter)




if __name__ == "__main__":
    app.run(debug=True)
