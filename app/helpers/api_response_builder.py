# api_response_builder.py
from flask import jsonify, make_response

def build_api_response(status, message, http_code, data=None):
    response = {
        'status': status,
        'message': message
    }
    
    if data:
        response['data'] = data

    return make_response(jsonify(response), http_code)
