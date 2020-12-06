from flask import Blueprint , render_template , request

main = Blueprint('main' , __name__)


@main.route('/home')
@main.route('/')
def home():
    return render_template('home.html' , title = 'Home Page')
