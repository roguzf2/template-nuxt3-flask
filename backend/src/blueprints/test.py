from flask import Blueprint, jsonify

test_data = [
    {
        'nome': 'Analytica',
        'ano': 2023
    },
    {
        'nome': 'UFRJ',
        'ano': 2022
    }
]

test = Blueprint('test', __name__)

@test.route('/test', methods=["GET"])
def get_test():
    return jsonify(test_data)