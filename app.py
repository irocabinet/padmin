from flask import Flask
from flask import Flask, render_template, request, redirect, url_for, session
from flask_bcrypt import Bcrypt #pip install Flask-Bcrypt = https://pypi.org/project/Flask-Bcrypt/
from werkzeug.utils import secure_filename
import os
from models import db, Users

app = Flask(__name__)

app.config['SECRET_KEY'] = 'cairocoders-ednalan'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskdb.db'
# Databse configuration mysql                             Username:password@hostname/databasename
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:''@localhost/library-system'
  
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True
   
bcrypt = Bcrypt(app) 
  
db.init_app(app)
         
with app.app_context():
    db.create_all()
 
 
app.config['UPLOAD_FOLDER'] = 'static/images'
    
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
    
def allowed_file(filename):
 return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/register', methods =['GET', 'POST'])
def register():
    # mesage = ''
    # if request.method == 'POST' and 'name' in request.form and 'password' in request.form and 'email' in request.form :
    #     fullname = request.form['name']
    #     password = request.form['password']
    #     email = request.form['email']
         
    #     user_exists = Users.query.filter_by(email=email).first() is not None
       
    #     if user_exists:
    #         mesage = 'Email already exists !'
    #     elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
    #         mesage = 'Invalid email address !'
    #     elif not fullname or not password or not email:
    #         mesage = 'Please fill out the form !'
    #     else:
    #         hashed_password = bcrypt.generate_password_hash(password)
    #         new_user = Users(name=fullname, email=email, password=hashed_password)
    #         db.session.add(new_user)
    #         db.session.commit()
    #         mesage = 'You have successfully registered !'
    # elif request.method == 'POST':
    #     mesage = 'Please fill out the form !'
    return render_template('register.html')

@app.route('/login', methods =['GET', 'POST'])
def login():
    # mesage = ''
    # if request.method == 'POST' and 'name' in request.form and 'password' in request.form and 'email' in request.form :
    #     fullname = request.form['name']
    #     password = request.form['password']
    #     email = request.form['email']
         
    #     user_exists = Users.query.filter_by(email=email).first() is not None
       
    #     if user_exists:
    #         mesage = 'Email already exists !'
    #     elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
    #         mesage = 'Invalid email address !'
    #     elif not fullname or not password or not email:
    #         mesage = 'Please fill out the form !'
    #     else:
    #         hashed_password = bcrypt.generate_password_hash(password)
    #         new_user = Users(name=fullname, email=email, password=hashed_password)
    #         db.session.add(new_user)
    #         db.session.commit()
    #         mesage = 'You have successfully registered !'
    # elif request.method == 'POST':
    #     mesage = 'Please fill out the form !'
    return render_template('login.html')
