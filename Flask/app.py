from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import mysql.connector

app = Flask(__name__)

# Replace the values below with your MySQL database credentials
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Hajna@2004",
  database="career_test"
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        fullname = request.form['fullname']
        grade = request.form['grade']
        question1 = request.form['question1']
        question2 = request.form['question2']
        question3 = request.form['question3']
        question4 = request.form['question4']
        question5 = request.form['question5']
        question6 = request.form['question6']
        question7 = request.form['question7']
        question8 = request.form['question8']
        question9 = request.form['question9']
        question10 = request.form['question10']
        question11 = request.form['question11']
        question12 = request.form['question12']

        mycursor = mydb.cursor()

        # Replace 'answers' with the name of your table
        sql = "INSERT INTO test (fullname, grade, question1, question2, question3, question4, question5, question6, question7, question8, question9, question10, question11, question12) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (fullname, grade, question1, question2, question3, question4, question5, question6, question7, question8, question9, question10, question11, question12)

        mycursor.execute(sql, val)
        mydb.commit()

        return "Data has been successfully submitted to the database!"

if __name__ == '__main__':
    app.run(debug=True)