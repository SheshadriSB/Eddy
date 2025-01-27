from flask import Flask
import threading
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run():
    port = int(os.environ.get("PORT", 8080))  # Use PORT from environment or default to 8080
    print(f"Running on port {port}")  # Add debugging to confirm the port
    app.run(host='0.0.0.0', port=port)


# Keep the bot alive by running the Flask app in a separate thread
def keep_alive():
    t = threading.Thread(target=run)
    t.start()
