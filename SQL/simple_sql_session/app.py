#!/usr/bin/python3
import os

from flask import Flask, render_template, request, redirect, url_for, session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)
app.secret_key ="Something"
##
engine = create_engine("mysql+pymysql://root:Junaid123@localhost:3306/python_for_web")


#engine = create_engine(\
#    "mysql+pymysql://root:Junaid123@localhost:3306/python_for_web"\
#    ,pool_size=20, max_overflow=0)


db = scoped_session(sessionmaker(bind=engine))

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == "POST":
        uname = request.form.get("uname")
        session['username'] = uname
        return redirect(url_for('index'))
    else:
        return render_template("login.html")
@app.route("/", methods=['GET'])
def index():
    if session.get('username'):
        if session['username'].lower() == "junaid":
            students = db.execute("SELECT * FROM students").fetchall()
            return render_template("intro.html", students=students)
        else:
            return "You don't have access to view this, <a href ='/login'> back to login </a>"
    else:
        return "Sorry! <a href='/login'> Login first </a>"

@app.route("/insert", methods=['GET'])
def insert():
    return render_template("insert_new_student.html")

@app.route("/intro", methods=['POST','GET'])
def intro():
    if request.method == "POST":

        name = request.form.get("name")
        email = request.form.get("email")
        program = request.form.get("program")
        db.execute("INSERT into students(full_name, email, batch_title) VALUES (:full_name, :email, :batch_title)",
                {"full_name": name, "email": email, "batch_title":program})
        db.commit()

        # Get all records again
        students = db.execute("SELECT * FROM students").fetchall()
        return render_template("intro.html", students=students)
    else:
        return "Sorry, please click <a href='/'> this </a> to view the record"

@app.route("/update/<int:id>/", methods=['POST','GET'])
def update(id):
    if request.method=="POST":
        name = request.form.get("name")
        email = request.form.get("email")
        program = request.form.get("program")
        db.execute("Update students SET full_name = :name , email = :email, batch_title = :program where id = :id",
                {"name": name, "email": email, "program":program, "id":id})
        db.commit()
        return redirect(url_for('index'))
    else:
        stud = db.execute("SELECT * FROM students WHERE id = :id", {"id": id}).fetchone()
        return render_template("update.html", stud=stud, id=id)


@app.route("/update_now/<int:id>/", methods=['POST', 'GET'])
def update_now(id):
    stud = db.execute("SELECT * FROM students WHERE id = :id", {"id": id}).fetchone()
    if stud is None:
        return "No record found by ID = " + str(id) +". Kindly go back to <a href='/intro'> Intro </a>"
    else:
        stud = db.execute("delete FROM students WHERE id = " + str(id))
        db.commit()
        return redirect(url_for('intro'))
@app.route("/delete/<int:id>/")
def delete(id):
    stud = db.execute("SELECT * FROM students WHERE id = :id", {"id": id}).fetchone()
    if stud is None:
        return "No record found by ID = " + str(id) +". Kindly go back to <a href='/intro'> Intro </a>"
    else:
        stud = db.execute("delete FROM students WHERE id = " + str(id))
        db.commit()
        return redirect(url_for('intro'))


if __name__ == "__main__":
    app.run(debug=True)
