from flask import Flask

app = Flask(__name__)


@app.route("/", methods=['GET'])
def my_index():
    return "Hello Word <br> Python for Web!!!"
@app.route("/test/hello/my_new_route", methods=['GET'])
def my_new_route():
    return "<h1> Hello Python Programmars!!!"




if __name__ == "__main__":
    app.run(debug=True)
