from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
#from flask_restplus import Api
import logging
from logging.handlers import RotatingFileHandler

from flask_zipkin import Zipkin

#zipkin = Zipkin(sample_rate=10)


from .config import config_by_name

toolbar = DebugToolbarExtension()

#api = Api()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    
    #init debug toolbar
    toolbar.init_app(app)
    #init api restplus
    #api.init_app(app)

    #zipkin.init_app(app)

    from inol_rest.home import home as home_blueprint
    app.register_blueprint(home_blueprint, url_prefix='/')

    from inol_rest.api import api_blueprint as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    #setup logging
    
    handler = RotatingFileHandler('C:/var/tmp/flask.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)


    return app