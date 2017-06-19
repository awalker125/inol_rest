from flask import Blueprint
from flask_restplus import Api
from flask_restplus import Resource
from flask_restplus import fields
from werkzeug.local import LocalProxy
from flask import current_app
from inol_rest.inol_calc.calculator import calculate_set_inol

logger = LocalProxy(lambda: current_app.logger)


api_blueprint = Blueprint('api', __name__)
api = Api(api_blueprint, version='1.0', title='INOL Rest API',
    description='REST Service for INOL (Intensity x Number Of Lifts)',
)

ns = api.namespace('inol', description='inol operations')


#from flask_restplus import reqparse

#inolRequestParser = reqparse.RequestParser()
#inolRequestParser.add_argument('reps', type=int, help='The number of reps in the set', location='json')
#inolRequestParser.add_argument('weight', type=float, help='he number weight of the set', location='json')
#inolRequestParser.add_argument('max', type=float, help='Current one rep max', location='json')

#args = inolRequestParser.parse_args()



inolRequest = api.model('inolRequest', {
    'reps': fields.Integer(required=True, description='The number of reps in the set'),
    'weight': fields.Float(required=True, description='The number weight of the set'),
    'max': fields.Float(required=True, description='Current one rep max')
})

inolResponse = api.model('inolResponse', {
    'reps': fields.Integer(required=True, description='The number of reps in the set'),
    'weight': fields.Float(required=True, description='The number weight of the set'),
    'max': fields.Float(required=True, description='Current one rep max'),
    'inol': fields.Float(description='The inol of the set')
})



@ns.route('/')
@api.doc()
class Inol(Resource):

    @api.marshal_with(inolResponse)
    @api.expect(inolRequest, validate=True)
    @api.response(200, 'Success', inolResponse)
    def post(self):

        logger.info("payload>>>\n {0}".format(api.payload))

        #inolRequest
        i = api.payload
        
        i['inol'] = calculate_set_inol(i['reps'],i['weight'],i['max'])
        
        #inolResponse = InolResponse(reps=data.reps)
        return i
        #return inolResponse(resp=10, weight=100.0, max=105.00, inol=0.8)