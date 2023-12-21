# Standard libraries
from io import BytesIO

# External libraries
from flask import Blueprint, send_file, g
import pandas as pd
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text

# Local imports
from src.utils import (
    connect_db,
)

# Create Blueprint
teste_bp = Blueprint("teste_bp", __name__)

# Create sessionmaker
Session = sessionmaker(
    bind = connect_db(),
    autoflush = True,
    autocommit = False
)

# Routes
@teste_bp.route("/rota-teste", methods=["GET"])
def func_teste():
    """ Função de GET na tabela Teste """
    # Map database tables as classes
    model = automap_base()
    model.prepare(connect_db(), reflect=True)

    # Perform query
    with Session() as session:
        try:
            # Query and convert the result to a list of dictionaries
            Test = model.classes.Test
            query_result = session.query(Test).all()
            results_list = []
            for teste_bp in query_result:
                teste_data = {}
                for column in Test.__table__.columns:
                    teste_data[column.name] = getattr(teste_bp, column.name)

                results_list.append(teste_data)
        except Exception as error:
            return {
                "detail": error.__class__.__name__ + ": " + error.__str__()
            }, 500

    return {
        "results": results_list
    }, 200
