import os
from flask import Flask
from . import db

"""
This File named as is; to tell Python that this directory '.flaskr/' should be treated as a package.  
"""


def create_app():
    """
    This function is known as the 'Application Factory'. Any configuration, registration, and other setup the
    application needs will happen inside this function, then the application will be returned.
    :param test_config:
    :return: Flask Application
    """
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True, template_folder='templates')
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)

    from . import vote
    app.register_blueprint(vote.bp)

    return app

