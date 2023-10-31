#!/usr/bin/python3

"""
Flask Application

This script defines a Flask application for the AirBnB clone Restful API. It configures the application, 
defines error handlers, and sets up CORS.

"""

from models import storage
from api.v1.views import app_views
from os import environ
from flask import Flask, render_template, make_response, jsonify
from flask_cors import CORS
from flasgger import Swagger
from flasgger.utils import swag_from

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})

@app.teardown_appcontext
def close_db(error):
    """
    Close Storage

    This function is a callback that Flask will call when the application context is being destroyed. 
    It is responsible for closing the database storage.

    Args:
        error: An optional error object.

    Returns:
        None
    """

storage.close()

@app.errorhandler(404)
def not_found(error):
    """
    404 Error

    This function is an error handler for HTTP 404 (Not Found) errors. It returns a JSON response 
    with an error message when a resource is not found.

    Returns:
        JSON response with a 404 error message.
    """
    return make_response(jsonify({'error': "Not found"}), 404)

app.config['SWAGGER'] = {
    'title': 'AirBnB clone Restful API',
    'uiversion': 3
}

Swagger(app)

if __name__ == "__main__":
    """
    Main Function

    This is the main entry point of the script. It configures and starts the Flask application.

    The following environment variables can be used to configure the application:
    - HBNB_API_HOST: Host for the application. Defaults to '0.0.0.0'.
    - HBNB_API_PORT: Port for the application. Defaults to '5000'.

    Returns:
        None
    """

    host = environ.get('HBNB_API_HOST')
    port = environ.get('HBNB_API_PORT')
    
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'

    app.run(host=host, port=port, threaded=True)

