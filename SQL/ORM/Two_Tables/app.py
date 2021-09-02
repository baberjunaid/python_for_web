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
app.config['SQLALCHEMY_ECHO'] = True
db.init_app(app)
class Students(db.Model):
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    batch_title = db.Column(db.Integer, nullable=False)
    date_created = db.Column(db.DATE, default=datetime.now())

class Student_Expertise(db.Model):
    __tablename__ = "student_expertise"
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(300), nullable=False)
    student_id = db.Column(db.Integer, nullable=False)
    date_created = db.Column(db.DATE, default=datetime.now())

@app.route("/", methods=['GET'])
def index():
    students = Students.query.all()
    return render_template("intro.html", students=students)

@app.route("/batch/<bt>", methods=['GET'])
def batch_filter(bt):
    students = Students.query.filter(Students.batch_title == bt).all()
    return render_template("intro.html", students=students)
@app.route("/search/<bt>/<name>", methods=['GET'])
def search(bt, name):
    students = Students.query.filter(Students.batch_title == bt)\
    .filter(Students.full_name == name).all()
    return render_template("intro.html", students=students)
@app.route("/student/expertise/<student_id>", methods=['GET', 'POST'])
def student_expertise(student_id):
    if request.method == "POST":
        topic = request.form.get("topic")
        stud_exp = Student_Expertise(student_id=student_id, topic=topic)
        db.session.add(stud_exp)
        db.session.commit()

    stud = Students.query.filter(Students.id == student_id).first()
    exp = Student_Expertise.query.filter(Student_Expertise.student_id == student_id).all()

    return render_template("student_expertise.html", exp=exp, student_id=student_id, stud=stud)
@app.route("/student/expertise_2/<student_id>", methods=['GET', 'POST'])
def student_expertise2(student_id):
    if request.method == "POST":
        topic = request.form.get("topic")
        stud_exp = Student_Expertise(student_id=student_id, topic=topic)
        db.session.add(stud_exp)
        db.session.commit()

    stud = db.session.query(Students, Student_Expertise)\
    .filter(Students.id == student_id)\
    .filter(Students.id == Student_Expertise.student_id).all()
    return render_template("student_expertise_2.html",  student_id=student_id, stud=stud)
@app.route("/student/expertise/view/all", methods=['GET'])
def student_expertise_view_all():

    stud = db.session.query(Students, Student_Expertise)\
    .filter(Students.id == Student_Expertise.student_id).all()
    return render_template("view_expertise.html",  stud=stud)

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
