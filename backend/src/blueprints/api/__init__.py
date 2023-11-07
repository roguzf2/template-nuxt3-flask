""" Sample blueprint """
# External libraries
from flask import (
    Blueprint,
    request,
    Response,
    jsonify
)

# Create blueprint
api_bp = Blueprint(
    name="api_bp",
    import_name=__name__
)

# Sample route
@api_bp.route("/", methods=["GET"])
def api_root() -> Response:
    """
    Sample route that returns the values it
    receives as query parameters
    """
    params = request.args

    results = [
        {
            "key": key,
            "value": value
        }
        for key, value
        in params.items()
    ]

    return jsonify(
        results
    )
