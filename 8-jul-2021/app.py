from flask import Flask, render_template

app = Flask(__name__)

@app.route("/old", methods=['GET','POST'])
def old():
    my_title = "Dynamic BSCS & IT"
    r = 5
    my_names = ['Ali', 'Usman', 'Jawad', 'Shazia','Bilal']
    return render_template("old_index.html", title = my_title,my_names =my_names, r = r)


@app.route("/", methods=['GET'])
def index():
    name = "John Smith"

    loop_iter = 3
    return render_template("index.html", name=name, loop_iter = loop_iter)




if __name__ == "__main__":
    app.run(debug=True)
