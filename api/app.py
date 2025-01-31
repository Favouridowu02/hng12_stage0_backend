import os
from flask import Flask,  make_response, jsonify
import json
from flask_cors import CORS
from datetime import datetime, timezone


# initialising the app
app = Flask(__name__)
CORS(app)

# defining the home route
@app.route('/', methods=['GET'])
def home():
    """
    This function returns a welcome message
    """
    return make_response(jsonify("Welcome to this api"))


# defining the api route
@app.route('/api', methods=['GET'])
def get_data():
    """
    This function return the basic information to the route
    """
    date = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    data = {
              'email': 'favouridowu02@gmail.com',
              'current_datetime': date,
              'github_url': 'https://github.com/Favouridowu02/hng12_stage0_backend'
            }

    return make_response(json.dumps(data))


if __name__ == '__main__':
    app.run(debug=True)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)