# Standard libraries
from os import getenv

# External libraries
from flask import request, g
import jwt
import sqlalchemy as sql
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.engine.base import Engine

def results_to_dict(results):
    try:
        return [result.dict for result in results]
    except AttributeError:
        return [result[0].dict for result in results]

def results_to_str(results):
    return [result.str() for result in results]

SQL_PORT="5432"
def connect_db() -> Engine:
    """Create engine to connect to database.

    Returns:
        Engine: The connection engine to the database.
    """
    return sql.create_engine(
        "postgresql://" +
        getenv('SQL_USER') +
        ":" +
        getenv('SQL_PSWD') +
        "@" +
        getenv('SQL_HOST') +
        ":" +
        SQL_PORT+
        "/" +
        getenv('SQL_DATABASE')
    )

def to_dict(self):
    columns = sql.inspect(self).mapper.column_attrs
    as_dict = {}
    for column in columns:
        as_dict[column.key] = getattr(self, column.key)
    return as_dict

def results_to_str(results):
    return [result.__str__() for result in results]

def treat_array_field(value):
    if value is None:
        return None
    if len(value) == 0:
        return None
    return (
        ", ".join(value)
    )

def treat_numeric_field(value):
    if value is None:
        return None
    return (
        int(
            str(value)
            .strip()
        )
    )

def treat_string_field(value):
    if value is None:
        return None
    if len(str(value)) == 0:
        return None
    return (
        str(value)
        .upper()
        .strip()
    )
    