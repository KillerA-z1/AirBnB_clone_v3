#!/usr/bin/python3
"""The controller for the api"""

from flask import Flask, jsonify, make_response
from models import storage
from api.v1.views import app_views
import os
from flask_cors import CORS

app = Flask(__name__)

app.register_blueprint(app_views)
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def teardown_db(exception):
    """
    Function to close the database connection after each request.

    Args:
            exceptions: The exception raised during the request.

    Returns:
            None
    """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """Handler for 404 errors that returns a JSON response"""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    HBNB_API_HOST = os.getenv("HBNB_API_HOST", "0.0.0.0")
    HBNB_API_PORT = int(os.getenv("HBNB_API_PORT", 5000))
    app.run(host=HBNB_API_HOST, port=HBNB_API_PORT, threaded=True)
