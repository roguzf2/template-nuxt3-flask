""" Main module for the backend server """
# External libraries
from flask import Flask
from flask_cors import CORS

# Local imports
from src.blueprints.api import api_bp
from src.blueprints.test import test

# Server instantiation and configuration
server = Flask(__name__)
server.config['JSON_SORT_KEYS'] = False
CORS(server)

# Blueprint registration
server.register_blueprint(
    api_bp,
    url_prefix="/api"
)
server.register_blueprint(
    test,
    url_prefix="/"
)

@server.get("/")
def root():
    """
    Simple route to check server status
    """
    return "Hello world!"
