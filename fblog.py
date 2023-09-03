from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'VinayPatil@248'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique = True, nullable = False)
    email = db.Column(db.String(50), unique = True, nullable = False)
    image_file = db.Column(db.String(20), unique = True, nullable = False, default = 'image.jpg')
    password = db.Column(db.String(50), nullable = False)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(60), nullble = False)
    content = db.column(db.Text, nullable = False)
    date_posted = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    user_id = db.Column(db.Inetger, db.Foreign_key('user.id') ,nullable = False)
    






#   db = SQLAlchemy(app)
#   class User(db.Model):
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blogdb.db'
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(15), unique=True, nullable = False)
#     email = db.Column(db.String(120), unique=True, nullable = False)
#     image_file = db.Column(db.String(20), unique=True, nullable = False, default = 'image.jpg')
#     password = db.Column(db.String(60), nullable = False)
#     posts = db.relationship('Post', backref = 'author', lazy=True)


#     def __repr__(self):
#         return f"User('{self.username}', '{self.email}', '{self.image_file}')"


# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(60), nullable = False)
#     date_posted = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
#     content = db.Column(db.Text, nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


#     def __repr__(self):
#         return f"Post('{self.title}', '{self.date_posted}')"






Post_details=[
        {
            'author': 'Vinay Patil',
            'title' : 'ML for begineers',
            'content' : 'about machine learning and fundamentals of ml stats and probability',
            'date_posted' : 'August 26 2023'
        },
        {
            'author': 'Vinay Patil',
            'title' : 'Cloud computing',
            'content' : 'Various cloud services',
            'date_posted' : 'August 25 2023'
        },
        {
            'author': 'Vinay Patil',
            'title' : 'Data Engineering',
            'content' : 'data etl',
            'date_posted' : 'August 24 2023'
        }
    ]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=Post_details)


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created Successfully for {form.username.data}!!', 'info')
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Register', form = form)

@app.route("/login", methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'vinay@gmail.com' and form.password.data == 'password':
            flash(f'Successfully Logged In!!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid Credentials', 'danger')
    return render_template('login.html', title = 'Login', form = form)


if __name__ == '__main__':
    app.run(debug=True)
