""" Main module for the backend server """
# External libraries
from flask import Flask, render_template
from flask_cors import CORS

# Local imports
from src.blueprints.api import api_bp
from src.blueprints.test import test
from src.blueprints.query import query_bp
from src.blueprints.query.teste import teste_bp
from src.blueprints.insert import insert_bp
from src.blueprints.insert.formularios import formularios_insert_bp

# Server instantiation and configuration
server = Flask(__name__)
server.config.sort_keys = False
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

server.register_blueprint(
    query_bp,
    url_prefix="/"
)

server.register_blueprint(
    teste_bp,
    url_prefix="/"
)

server.register_blueprint(
    insert_bp,
    url_prefix="/"
)

server.register_blueprint(
    formularios_insert_bp,
    url_prefix="/"
)

@server.route("/", methods=["GET"])
def root():
    """
    Simple route to check server status
    """
    return render_template("homepage.html")
