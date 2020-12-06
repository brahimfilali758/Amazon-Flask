from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_socketio import SocketIO


db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()
socketio = SocketIO()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '3a83b21b509197e1b3be5571bf594e55'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    socketio.init_app(app)

    from flaskamazon.main.routes import main
    from flaskamazon.users.routes import users
    from flaskamazon.events import chat

    app.register_blueprint(main)
    app.register_blueprint(users)

    return app
