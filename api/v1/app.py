#!/usr/bin/python3
"""The controller for the api"""

from flask import Flask, jsonify, make_response
from models import storage
from api.v1.views import app_views
import os

app = Flask(__name__)

app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Function to close the database connection after each request.

    Args:
            exception: The exception raised during the request.

    Returns:
            None
    """
    storage.close()


if __name__ == "__main__":
    HBNB_API_HOST = os.getenv("HBNB_API_HOST", "0.0.0.0")
    HBNB_API_PORT = int(os.getenv("HBNB_API_PORT", 5000))
    app.run(host=HBNB_API_HOST, port=HBNB_API_PORT, threaded=True)
