import uuid

from flask_restplus import Resource

from inol_rest.api import api
from inol_rest.api import logger
from inol_rest.api.models import inol_response, inol_request, training_model, training_option, training_options_request, training_options_response, training_plan_request, training_plan_response, training_session
from inol_rest.api.core import calculate_set_inol_weight, generate_training_options, generate_training_plan

calc = api.namespace('calc', description='calculators')
training = api.namespace('training', description='training operations')





@calc.route('/inol')
@api.doc()
class Inol(Resource):

    @api.marshal_with(inol_response)
    @api.expect(inol_request, validate=True)
    @api.response(200, 'Success', inol_response)
    def post(self):

        tracking_id = uuid.uuid4()
        
        logger.info("{0} payload {1}".format(tracking_id, api.payload))

        # inboundRequest
        i = api.payload
        
        i['inol'] = calculate_set_inol_weight(i['reps'], i['weight'], i['maximum'])
        i['tracking_id'] = tracking_id
        
        # inol_response = inol_response(reps=data.reps)
        return i


# Test message
# {
#   "min_set_inol": 0.05,
#   "intensity": 80,
#   "min_exercise_inol": 0.3,
#   "max_exercise_inol": 2,
#   "maximum": 182.5,
#   "max_sets": 6,
#   "max_reps": 12,
#   "max_set_inol": 0.5
# }

#curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' -d '{ "min_set_inol": 0.05, "intensity": 80, "min_exercise_inol": 0.3, "max_exercise_inol": 2, "maximum": 182.5, "max_sets": 6, "max_reps": 12, "max_set_inol": 0.5 }' 'http://walandre9:5000/api/training/options'







@training.route('/options')
@api.doc()
class training_options(Resource):

    @api.marshal_with(training_options_response)
    @api.expect(training_options_request, validate=True)
    @api.response(200, 'Success', training_options_response)
    def post(self):

        tracking_id = uuid.uuid4()
        
        logger.info("{0} payload {1}".format(tracking_id, api.payload))

        # inboundRequest
        i = api.payload
        # current_max, max_reps, intensity,  max_sets, min_set_inol, max_set_inol, min_exercise_inol, max_exercise_inol
        training_options = generate_training_options(
            i['intensity'],
            i['maximum'],
            i['max_reps'],
            i['max_sets'],
            i['min_set_inol'],
            i['max_set_inol'],
            i['min_exercise_inol'],
            i['max_exercise_inol'])
        i['training_options'] = training_options
        i['tracking_id'] = tracking_id
        
        return i





# {
#     "training_model": {
#         "training_sessions": [
#             {
#                 "week": 1,
#                 "intensity": 65,
#                 "target_exercise_inol": 0.8
#             }, {
#                 "week": 2,
#                 "intensity": 70,
#                 "target_exercise_inol": 0.9
#             }, {
#                 "week": 3,
#                 "intensity": 75,
#                 "target_exercise_inol": 1.0
#             }, {
#                 "week": 4,
#                 "intensity": 80,
#                 "target_exercise_inol": 0.8
#             }, {
#                 "week": 5,
#                 "intensity": 85,
#                 "target_exercise_inol": 0.9
#             }, {
#                 "week": 6,
#                 "intensity": 90,
#                 "target_exercise_inol": 1.0
#             }, {
#                 "week": 7,
#                 "intensity": 95,
#                 "target_exercise_inol": 0.8
#             }
#         ]
#     },
#     "name": "bench",
#     "max": 182.5,
#     "max_sets": 6,
#     "max_reps": 12,
#     "min_exercise_inol": 0.3,
#     "max_exercise_inol": 2,
#     "min_set_inol": 0.05,
#     "max_set_inol": 0.5
# }


# curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' -d '{ \ 
#      "training_model": { \ 
#          "training_sessions": [ \ 
#              { \ 
#                  "week": 1, \ 
#                  "intensity": 65, \ 
#                  "target_exercise_inol": 0.8 \ 
#              }, { \ 
#                  "week": 2, \ 
#                  "intensity": 70, \ 
#                  "target_exercise_inol": 0.9 \ 
#              }, { \ 
#                  "week": 3, \ 
#                  "intensity": 75, \ 
#                  "target_exercise_inol": 1.0 \ 
#              }, { \ 
#                  "week": 4, \ 
#                  "intensity": 80, \ 
#                  "target_exercise_inol": 0.8 \ 
#              }, { \ 
#                  "week": 5, \ 
#                  "intensity": 85, \ 
#                  "target_exercise_inol": 0.9 \ 
#              }, { \ 
#                  "week": 6, \ 
#                  "intensity": 90, \ 
#                  "target_exercise_inol": 1.0 \ 
#              }, { \ 
#                  "week": 7, \ 
#                  "intensity": 95, \ 
#                  "target_exercise_inol": 0.8 \ 
#              } \ 
#          ] \ 
#      }, \ 
#      "name": "bench", \ 
#      "max": 182.5, \ 
#      "max_sets": 6, \ 
#      "max_reps": 12, \ 
#      "min_exercise_inol": 0.3, \ 
#      "max_exercise_inol": 2, \ 
#      "min_set_inol": 0.05, \ 
#      "max_set_inol": 0.5 \ 
#  }' 'http://walandre9:5000/api/training/plan'

@training.route('/plan')
@api.doc()
class TrainingPlan(Resource):

    @api.marshal_with(training_plan_response)
    @api.expect(training_plan_request, validate=True)
    @api.response(200, 'Success', training_plan_response)
    def post(self):

        tracking_id = uuid.uuid4()
        
        logger.info("{0} payload {1}".format(tracking_id, api.payload))

        # inboundRequest
        i = api.payload
        
        training_plan = generate_training_plan(
            
            #name, maximum, max_reps, max_sets, min_set_inol, max_set_inol, min_exercise_inol, max_exercise_inol, training_model
            i['name'],
            i['maximum'],
            i['max_reps'],
            i['max_sets'],
            i['min_set_inol'],
            i['max_set_inol'],
            i['min_exercise_inol'],
            i['max_exercise_inol'],
            i['training_model']
            )
        
        
        i['training_plan'] = training_plan
        i['tracking_id'] = tracking_id
        
        return i
