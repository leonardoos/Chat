from flask import Flask
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mys3cr31'
socketio = SocketIO(app)

@socketio.on('message')
def handlem(msg):
    print("Message {}".format(msg))
    send(msg, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
