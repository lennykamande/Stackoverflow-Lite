from flask import Flask, Blueprint, request, redirect,jsonify



def create_app(env="dev"):

    # Initialize the application
    app = Flask(__name__)
    
    from .resources.questions import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')

    from .resources.answers import answer_api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')

    from .resources.users import user_api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1/')

    return app








