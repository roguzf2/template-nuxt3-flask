""" Main module for the backend server """
# External libraries
from flask import Flask
from flask_cors import CORS

# Local imports
from src.blueprints.api import api_bp

# Server instantiation and configuration
server = Flask(__name__)
server.config['JSON_SORT_KEYS'] = False
CORS(server)

# Blueprint registration
server.register_blueprint(
    api_bp,
    url_prefix="/api"
)

@server.get("/")
def root():
    """
    Simple route to check server status
    """
    return "Hello world!"
