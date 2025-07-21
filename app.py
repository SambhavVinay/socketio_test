from flask import Flask, request, render_template, redirect
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = "jhqsfi"
socketio = SocketIO(app)

@app.route("/")
def home():
    return render_template("home.html")

@socketio.on("message")
def handle_message(msg):
    print("received message : "+ msg)
    send(msg, broadcast = True)

if __name__ == "__main__":
    socketio.run(app, debug=True)
