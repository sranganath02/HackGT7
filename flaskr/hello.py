from flask import Flask, Response
from flask import request
import mysql.connector
import uuid

cnx = mysql.connector.connect(user='root', password='dreamTeam135',
                              host='104.198.46.183',
                              database='users')
cnx.database = 'users'
cursor = cnx.cursor()
#import re

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/create', methods=['POST'])
def create():
    if request.method == 'POST':
        print(request.form)
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        birthDate = request.form['birthDate']
        max = 50
        #regex_email = '[^@]+@[^@]+\.[^@]+'
        
        if len(firstName) > max and len(lastName) > max and len(username) > max and len(password) > max and len(
                birthDate) > max:
            return "Record not found", 400
        # if not re.search(regex_email, email):
        #    return "Record not found email", 400

        data = [firstName, lastName, username, password, email, birthDate]
        print(data)
        #Create a way to generate unique id everytime
        cursor.execute("INSERT INTO users (firstName, lastName ,username, password, email, birthDate) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}')".format(
            data[0], data[1], data[2], data[3], data[4], data[5]))
        cnx.commit()
        return "Success", 200
