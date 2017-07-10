from flask import Blueprint
from flask_restplus import Api
from flask_restplus import Resource
from flask_restplus import fields
from werkzeug.local import LocalProxy
from flask import current_app
from inol_rest.inol_calc.calculator import calculate_set_inol
import uuid
import math


logger = LocalProxy(lambda: current_app.logger)


api_blueprint = Blueprint('api', __name__)
api = Api(api_blueprint, version='1.0', title='INOL Rest API',
    description='REST Service for INOL (Intensity x Number Of Lifts)',
)

#this has to come after the api is defined as we have a circular reference. As painful as this is, its cleaner than having everything in one file.
#from inol_rest.api.models import inolResponse, inolRequest, trainingModel, trainingOption, trainingOptionsRequest, trainingOptionsResponse, trainingPlanRequest, trainingPlanResponse, trainingSession

from inol_rest.api.views import calc, training