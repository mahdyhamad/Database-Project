import os
from flask import Flask

"""
This File named as is; to tell Python that this directory '.flaskr/' should be treated as a package.  
"""


def create_app(test_config=None):
    """
    This function is known as the 'Application Factory'. Any configuration, registration, and other setup the
    application needs will happen inside this function, then the application will be returned.
    :param test_config:
    :return: Flask Application
    """
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    from . import db
    db.init_app(app)

    from . import voting_form
    app.register_blueprint(voting_form.bp)

    return app

