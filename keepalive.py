from flask import Flask
import threading
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run():
    # Render typically sets PORT as an environment variable
    port = int(os.environ.get("PORT", 8080))  # Default to 8080 if PORT is not set
    print(f"Flask app running on port {port}")
    app.run(host='0.0.0.0', port=port)  # Ensure binding to 0.0.0.0

def keep_alive():
    # Start Flask app in a separate thread
    t = threading.Thread(target=run)
    t.start()
