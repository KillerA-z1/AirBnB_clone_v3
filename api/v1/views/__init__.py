#!/usr/bin/python3
"""
This module initializes the views for the API version 1.

It creates a Flask Blueprint object named 'app_views' with
the URL prefix '/api/v1'.
The Blueprint object is used to define routes and views for the API.

The module also imports the views from the 'index' module, which contains
the routes and views for the index endpoint.
"""

from flask import Blueprint
from api.v1.views.index import *

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
