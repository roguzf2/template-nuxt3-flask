"""Blueprint for database query routes"""

# External libraries
from flask import Blueprint, request
import pandas as pd
import sqlalchemy as sql
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker

# Local imports
from src.utils import connect_db

# Create Blueprint
insert_bp = Blueprint("insert_bp", __name__)

# Create sessionmaker
Session = sessionmaker(
    bind = connect_db(),
    autoflush = True,
    autocommit = False
)