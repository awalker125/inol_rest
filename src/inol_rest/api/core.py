import math
from inol_rest.api import logger


# these are ordinary functions functions that calculate stuff. 


def getInolDifference(target_exercise_inol, exercise_inol):
    return math.fabs(target_exercise_inol - exercise_inol)
    
def roundPowerlifting(x, precision=1, base=2.5):
    return round(base * round(float(x) / base), precision)

def roundOlympiclifting(x, precision=0, base=1):
    return round(base * round(float(x) / base), precision)    


def calculate_set_inol_weight(reps, weight, maximum):
    intensity = float(weight) / float(maximum) * 100
    logger.debug("intensity: {0}".format(str(intensity)))   
    return calculate_set_inol(reps, intensity)
    
def calculate_set_inol(reps, intensity):
    logger.debug("reps {0}".format(str(reps)))
    logger.debug("intensity {0}".format(str(intensity)))   
    return float(reps) / (100 - intensity)

def generate_training_options(intensity, maximum, max_reps, max_sets, min_set_inol, max_set_inol, min_exercise_inol, max_exercise_inol):
    min_sets = 1
    training_options = []
    for r in range(1, max_reps + 1):
        logger.debug("using reps {0}".format(str(r)))
        set_inol = calculate_set_inol(r, intensity)
        logger.debug("set inol for {0} rep(s) @ {1} is {2}".format(str(r), str(intensity), str(set_inol)))
        for s in range(min_sets, max_sets + 1):
            exercise_inol = set_inol * s
            volume = r * s
            weight = maximum * (float(intensity) / 100)
            weight_powerlifting = roundPowerlifting(weight)
            weight_olympic = roundOlympiclifting(weight)
            scheme = str(s) + "x" + str(r) + "@" + str(intensity) + "%"
            if set_inol > min_set_inol:
                logger.debug("set_inol {0} > min_set_inol {1}".format(str(set_inol), str(min_set_inol)))
                if set_inol < max_set_inol:
                    logger.debug("set_inol {0} < max_set_inol {1}".format(str(set_inol), str(max_set_inol)))
                    if exercise_inol > min_exercise_inol:
                        logger.debug("exercise_inol {0} > min_exercise_inol {1}".format(str(exercise_inol), str(min_exercise_inol)))
                        if exercise_inol < max_exercise_inol:
                            logger.debug("exercise_inol {0} < max_exercise_inol {1}".format(str(exercise_inol), str(max_exercise_inol)))
                            to = {}
                            to['scheme'] = scheme
                            to['exercise_inol'] = exercise_inol
                            to['set_inol'] = set_inol
                            to['volume'] = volume
                            to['weight'] = weight
                            to['weight_powerlifting'] = weight_powerlifting
                            to['weight_powerlifting'] = weight_powerlifting
                            to['weight_olympic'] = weight_olympic
                            logger.debug("training_option >>> " + str(to))
                            training_options.append(to)

    logger.debug(training_options)
    return training_options


def generate_training_plan(name, maximum, max_reps, max_sets, min_set_inol, max_set_inol, min_exercise_inol, max_exercise_inol, training_model):
    
    training_plan = []
    training_sessions = training_model['training_sessions']
    
    for training_session in training_sessions:
        best_training_option = get_best_training_option(name, maximum, max_reps, max_sets, min_set_inol, max_set_inol, min_exercise_inol, max_exercise_inol, training_session['week'], training_session['intensity'], training_session['target_exercise_inol'])
        training_plan.append(best_training_option)
    
    sorted_training_plan = sorted(training_plan, key=lambda k: (k['week']))
    
    return sorted_training_plan



def get_best_training_option(name, maximum, max_reps, max_sets, min_set_inol, max_set_inol, min_exercise_inol, max_exercise_inol, week, intensity, target_exercise_inol):
    
    
    training_options = generate_training_options(intensity, maximum, max_reps, max_sets, min_set_inol, max_set_inol, min_exercise_inol, max_exercise_inol)
    
    # sort by overall excercise inol, then set inol, then volume.
    # this will order options into easiest to hardest and may mean sessions take longer.
    # sorted_training_options = sorted(training_options, key=lambda k: (k['exercise_inol'],k['set_inol'],k['volume'] ))
    
    best_training_option = None
    for training_option in training_options:
            
            # print training_option['exercise_inol']
            
        if best_training_option is None:
                best_training_option = training_option
        else:
                # print training_option
                # print best_training_option
            best_difference = getInolDifference(target_exercise_inol, best_training_option['exercise_inol']);
            training_option_difference = getInolDifference(target_exercise_inol, training_option['exercise_inol']);
                
            if training_option_difference < best_difference:
                logger.info("Option {2} is better {1} < {0}: ".format(str(best_difference), str(training_option_difference), str(training_option['scheme'])))
                best_training_option = training_option
            else:
                logger.info("Option {2} is worse {1} > {0}: ".format(str(best_difference), str(training_option_difference), str(training_option['scheme'])))
                
            
        logger.info("found best training {0} option for week {1}s".format(str(best_training_option), str(week)))
        
        best_training_option["week"] = week
    
    return best_training_option