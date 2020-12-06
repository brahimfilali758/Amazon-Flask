from flask import request
from flask_login import current_user
from flaskamazon import socketio
from flask_socketio import join_room , leave_room



@socketio.on('connect')
def connect():
    print(f' The session id is :  {request.sid}')
    print('User Connected')

