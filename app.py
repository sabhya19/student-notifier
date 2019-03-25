from flask import Flask, render_template, flash , redirect, url_for, session, logging, request
from wtforms import Form, StringField, PasswordField, validators
from pymongo import *

app=Flask(__name__)
client = MongoClient('mongodb+srv://vedaant:vedaant123@studentnotifier-fx3dd.gcp.mongodb.net/test?retryWrites=true')
users = ["admin", "dean","test"]
password = "1234"



# index route
@app.route('/')
def index():
    return render_template('index.html')
#end index route

#about route

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/notice')
def notice():
    if 'username' in session:
        username = session['username']
        return render_template("notice.html", user=username)
    else:
        return "You are not logged in <br><a href = '/login'></b>" + \
      "click here to log in</b></a>"

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        username = session['username']
        return render_template("dashboard.html", user=username)
    else:
        return "You are not logged in <br><a href = '/login'></b>" + \
      "click here to log in</b></a>"

#login route

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username=request.form['username']
        Password=request.form['password']
        while Password=="123456":
            session['username']=request.form['username']
            if username=="admin":
                return redirect(url_for('notice'))
            elif username == "dean":
                return redirect(url_for('dashboard'))
            else:
                flash("enter correct password")
                
        print(username, Password)


    return render_template('login1.html')

@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('username', None)
   return redirect(url_for('index'))



# database configs 

db = client['test-database']
collection = db['test-collection']


# running on the server 
if __name__ == '__main__':
    app.secret_key='secret123'
    app.run(debug=True)