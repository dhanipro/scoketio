from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret!'
    socketio = SocketIO(app)

    @app.route('/')
    def home():
        return render_template('index.html', async_mode=socketio.async_mode)

    @socketio.on('message')
    def send_message(message):
        send(message)

    @socketio.event
    def my_ping():
        emit('my_pong')
    
    return app