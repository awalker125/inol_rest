from flask import Blueprint

home = Blueprint('home', __name__)

from inol_rest.home import views
