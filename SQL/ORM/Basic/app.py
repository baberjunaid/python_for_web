#!/usr/bin/python3
import os

from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
##postgress
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:Junaid123@localhost:3306/python_for_web"
app.config['SECRET_KEY'] = "random string"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
class Students(db.Model):
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    batch_title = db.Column(db.Integer, nullable=False)
    date_created = db.Column(db.DATE, default=datetime.now())

@app.route("/", methods=['GET'])
def index():
    students = Students.query.all()
    return render_template("intro.html", students=students)

@app.route("/batch/<bt>", methods=['GET'])
def batch_filter(bt):
    students = Students.query.filter(Students.batch_title == bt).all()
    return render_template("intro.html", students=students)

@app.route("/insert", methods=['GET', 'POST'])
def insert():
    if request.method == "POST":

        name = request.form.get("name")
        email = request.form.get("email")
        program = request.form.get("program")

        # Creat new record
        stud = Students(full_name = name, email=email, batch_title=program)
        db.session.add(stud)
        db.session.commit()

        students = Students.query.all()
        return render_template("intro.html", students=students)


    return render_template("insert_new_student.html")

@app.route("/intro", methods=['POST', 'GET'])
def intro():
    if request.method == "POST":

        name = request.form.get("name")
        email = request.form.get("email")
        program = request.form.get("program")

        # Get all records again
        students = Students.query.all()
        return render_template("intro.html", students=students)
    else:
        students = Students.query.all()
        return render_template("intro.html", students=students)
@app.route("/update/<int:id>/", methods=['POST','GET'])
def update(id):
    if request.method=="POST":
        name = request.form.get("name")
        email = request.form.get("email")
        program = request.form.get("program")

        stud = Students.query.filter_by(id = id).first()
        stud.full_name = name
        stud.email = email
        stud.batch_title = program
        db.session.commit()
        return redirect(url_for('intro'))
    else:
        stud = Students.query.filter(Students.id == id).first()
        return render_template("update.html", stud=stud, id=id)

if __name__ == "__main__":
    app.run(debug=True)
