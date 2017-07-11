from inol_rest.api import api
from flask_restplus import fields

# Models

trainingOption = api.model('trainingOption', {   
                               "scheme": fields.String(description='Training schema set x reps @ intensity'),
                               "exercise_inol": fields.Float(description='The total exercise inol'),
                               "set_inol": fields.Float(description='The set inol'),
                               "volume": fields.Integer(description='Total volume'),
                               "weight": fields.Float(description='Weight (exact)'),
                               "weight_powerlifting": fields.Float(description='Weight (rounded to 2.5kg)'),
                               "weight_olympic": fields.Float(description='Weight (rounded to 1kg)')
                            }
                           )



trainingSession = api.model('trainingSession',
                           {   
                               "week": fields.Integer(description='Training week'),
                               "intensity": fields.Float(description='The training intensity'),
                               "target_exercise_inol": fields.Float(description='The target exercise inol')
                            }
                           )

trainingModel = api.model('trainingModel',
                           {   
                               "trainingSessions": fields.List(fields.Nested(trainingSession), description='Training sessions which make up the overall model'),
                            }
                           )
# Models Request

inolRequest = api.model('inolRequest', {
    'reps': fields.Integer(required=True, description='The number of reps in the set'),
    'weight': fields.Float(required=True, description='The number weight of the set'),
    'maximum': fields.Float(required=True, description='Current one rep max')
})

trainingOptionsRequest = api.model('trainingOptionsRequest', {
    # current_max, max_reps, intensity, min_sets, max_sets, min_set_inol, max_set_inol, min_exercise_inol, max_exercise_inol
    'intensity': fields.Float(required=True, description='The training intensity to generate options for. e.g 80%'),
    'maximum': fields.Float(required=True, description='Current one rep max'),
    'max_reps': fields.Integer(required=True, description='The maximum number of reps per set.'),
    'max_sets': fields.Integer(required=True, description='The maximum number of sets'),
    'min_set_inol': fields.Float(required=True, description='The minimum set inol to consider'),
    'max_set_inol': fields.Float(required=True, description='The maximum set inol to consider'),
    'min_exercise_inol': fields.Float(required=True, description='The minimum exercise inol to consider'),
    'max_exercise_inol': fields.Float(required=True, description='The minimum exercise inol to consider')
})



trainingPlanRequest = api.model('trainingPlanRequest', {
    # current_max, max_reps, intensity, min_sets, max_sets, min_set_inol, max_set_inol, min_exercise_inol, max_exercise_inol
    'name': fields.String(required=True, description='Exercise name e.g bench'),
    'maximum': fields.Float(required=True, description='Current one rep max'),
    'max_reps': fields.Integer(required=True, description='The maximum number of reps per set.'),
    'max_sets': fields.Integer(required=True, description='The maximum number of sets'),
    'min_set_inol': fields.Float(required=True, description='The minimum set inol to consider'),
    'max_set_inol': fields.Float(required=True, description='The maximum set inol to consider'),
    'min_exercise_inol': fields.Float(required=True, description='The minimum exercise inol to consider'),
    'max_exercise_inol': fields.Float(required=True, description='The minimum exercise inol to consider'),
    'trainingModel' : fields.Nested(trainingModel, required=True,description='The training model')
})

# Models Responses

inolResponse = api.model('inolResponse', {
    'reps': fields.Integer(required=True, description='The number of reps in the set'),
    'weight': fields.Float(required=True, description='The number weight of the set'),
    'maximum': fields.Float(required=True, description='Current one rep max'),
    'inol': fields.Float(description='The inol of the set'),
    'tracking_id': fields.String(required=True, description="Tracking id")
})



trainingOptionsResponse = api.model('trainingOptionsResponse', {
    'intensity': fields.Float(required=True, description='The training intensity to generate options for. e.g 80%'),
    'maximum': fields.Float(required=True, description='Current one rep max'),
    'max_reps': fields.Integer(required=True, description='The maximum number of reps per set.'),
    'max_sets': fields.Integer(required=True, description='The maximum number of sets'),
    'min_set_inol': fields.Float(required=True, description='The minimum set inol to consider'),
    'max_set_inol': fields.Float(required=True, description='The maximum set inol to consider'),
    'min_exercise_inol': fields.Float(required=True, description='The minimum exercise inol to consider'),
    'max_exercise_inol': fields.Float(required=True, description='The minimum exercise inol to consider'),
    'training_options': fields.List(fields.Nested(trainingOption), description='The training options'),
    'tracking_id': fields.String(required=True, description="Tracking id")
})

trainingPlanResponse = api.model('trainingPlanResponse', {
    'intensity': fields.Float(required=True, description='The training intensity to generate options for. e.g 80%'),
    'maximum': fields.Float(required=True, description='Current one rep max'),
    'max_reps': fields.Integer(required=True, description='The maximum number of reps per set.'),
    'max_sets': fields.Integer(required=True, description='The maximum number of sets'),
    'min_set_inol': fields.Float(required=True, description='The minimum set inol to consider'),
    'max_set_inol': fields.Float(required=True, description='The maximum set inol to consider'),
    'min_exercise_inol': fields.Float(required=True, description='The minimum exercise inol to consider'),
    'max_exercise_inol': fields.Float(required=True, description='The minimum exercise inol to consider'),
    'training_options': fields.List(fields.Nested(trainingOption), description='The training options'),
    'tracking_id': fields.String(required=True, description="Tracking id")
})