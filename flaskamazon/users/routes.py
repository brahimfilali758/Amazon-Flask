from flask import Blueprint , render_template , redirect , url_for , flash
from flaskamazon import db , login_manager , bcrypt
from flaskamazon.models import User , Seller , Product
from flaskamazon.users.utils import get_random_string , get_random_email
from flask_login import login_user , logout_user , current_user
from .forms import RegistrationForm , LoginForm

users = Blueprint('users' , __name__)

@users.route('/register/client',methods = ['GET','POST'])
def register_client():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        random_user = User(username=form.username.data,email=form.email.data,password=hashed_pass)
        db.session.add(random_user)
        db.session.commit()
        return redirect(url_for('users.login'))
    return render_template('register.html' , title = 'Register Today !' , form = form)

@users.route('/register/seller',methods = ['GET','POST'])
def register_seller():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        random_user = Seller(username=form.username.data,email=form.email.data,password=hashed_pass)
        db.session.add(random_user)
        db.session.commit()
        return redirect(url_for('users.login'))
    return render_template('register.html' , title = 'Register Today !' , form = form)

@users.route('/login',methods = ['GET','POST'])
def login():
    if current_user.is_authenticated :
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user)
            flash('You have Logged in succefully' , 'info')
            return redirect(url_for('main.home'))
    return render_template('login.html' ,title = 'Login Now !' , form = form )

@users.route('/logout')
def logout():
    logout_user()
    flash('You have Logged out succefully' , 'info')
    return redirect(url_for('main.home'))


@users.route('/<username>/chat')
def chat(username):
    user_to_message = User.query.filter_by(username=username).first
    if user_to_message :
        pass
    return render_template('chat.html' , user_to_message=user_to_message)


@users.route('/<username>')
def profile(username):
    user=User.query.filter_by(username=username).first()
    return render_template('profile.html')

