#!/usr/bin/python3
"""
Flask App that integrates with AirBnB static HTML Template
"""
from models import storage
from api.v1.views import app_views
from os import environ
from flask import Flask, render_template, make_response, jsonify
from flask_cors import CORS

# Global Flask Application Variable: app
app = Flask(__name__)

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

# app_views BluePrint defined in api.v1.views
app.register_blueprint(app_views)

# Cross-Origin Resource Sharing
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})

# begin flask page rendering
@app.teardown_appcontext
def close_db(error):
    """ Close Storage """
    storage.close()

@app.errorhandler(404)
def not_found(error):
    """
    handles 404 errors, in the event that global error handler fails
    ---
    responses:
      404:
        description: a resource was not found
    """
    return make_response(jsonify({'error': "Not found"}), 404)

if __name__ == "__main__":
    """ Main Function """
    host = environ.get('HBNB_API_HOST')
    port = environ.get('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)
