from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'joel-ghana-2026'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('join')
def on_join(data):
    emit('message', {'name': 'SYSTEM', 'msg': f"{data['name']} joined! 🇬🇭"}, broadcast=True)

@socketio.on('chat')
def on_chat(data):
    emit('message', data, broadcast=True)

if __name__ == '__main__':
    print("=== JOEL's WHATSAPP LIVE ===")
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)