# filepath: /home/favour/hng12_stage0_backend/app.py
import os
from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime, timezone
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    """
    This function returns a JSON response with email, current datetime, and GitHub URL.
    """
    information = {
        "email": os.getenv("EMAIL"),
        "current_datetime": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "github_url": os.getenv("GITHUB_URL"),
    }
    return jsonify(information), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)