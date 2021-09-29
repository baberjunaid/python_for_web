from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    my_data = {"English": 70, "Pak-Studies": 75, "Programming Fundamentals": 50}
    stud={}
    stud["Asad Ullah"] = {"English": 70, "Pak-Studies": 75, "Programming Fundamentals": 50}
    stud["Balach Rahim"] = {"English": 80, "Pak-Studies": 65, "Programming Fundamentals": 60}
    stud["Rabia Ihsan"] = {"English": 80, "Pak-Studies": 75, "Programming Fundamentals": 70}
    stud["Muhammad Harris"] = {"English": 50, "Pak-Studies": 95, "Programming Fundamentals": 60}

    loop_iter = 3
    return render_template("index.html", stud = stud)

@app.route("/my_chart", methods=['GET'])
def my_chart():

    my_data = {"English": 70, "Pak-Studies": 75, "Programming Fundamentals": 50}


    return render_template("myChart.html", my_data=my_data)




if __name__ == "__main__":
    app.run(debug=True)
