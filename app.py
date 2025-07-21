from flask import Flask, render_template
from flask_socketio import SocketIO, send
import eventlet
eventlet.monkey_patch()  # <-- Add this line at the top

app = Flask(__name__)
app.config['SECRET_KEY'] = "jhqsfi"
socketio = SocketIO(app)

@app.route("/")
def home():
    return render_template("home.html")

@socketio.on("message")
def handle_message(msg):
    print("received message : " + msg)
    send(msg, broadcast=True)

# Remove this block — Render won't use it
# if __name__ == "__main__":
#     socketio.run(app, debug=True)
