from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask (__name__,template_folder='templates')

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'ssh-agent'
app.config['MYSQL_DB'] = 'parents'

mysql = MySQL(app)

@app.route('/', methods = ['GET'])
def main():
    return render_template('index.html')

@app.route('/insertintodatabase', methods=['POST'])
def index():
    if request.method == "POST":
        details = request.form
        motherName = details['motherName']
        fatherName = details['fatherName']
        firstNameofChild = details['firstNameofChild']
        groupName = details['groupName']
        email = details['email']
        password = details['password']
        cursor = mysql.connection.cursor()
        values = (motherName, fatherName, firstNameofChild, groupName, email, password,)
        cursor.execute("INSERT INTO parents (motherName, fatherName, firstNameofChild, groupName, email, password) VALUES (%s, %s, %s, %s, %s, %s)", values)
        mysql.connection.commit()
        cursor.close()
        return 'success'
    return render_template('index.html')


if __name__ == 'main':
    app.run()
