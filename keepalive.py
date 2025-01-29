from flask import Flask
from threading import Thread
from waitress import serve
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run_server():
    port = int(os.environ.get("PORT", 8080))
    serve(app, host='0.0.0.0', port=port)

def keep_alive():
    server_thread = Thread(target=run_server)
    server_thread.daemon = True
    server_thread.start()
