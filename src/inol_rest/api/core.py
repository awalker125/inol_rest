import math
from inol_rest.api import logger


#these are ordinary functions functions that calculate stuff. 


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

def generate_training_options(current_max, max_reps, intensity, max_sets, min_set_inol, max_set_inol, min_exercise_inol, max_exercise_inol):
    min_sets = 1
    training_options = []
    for r in range(1, max_reps + 1):
        logger.debug("using reps {0}".format(str(r)))
        set_inol = calculate_set_inol(r, intensity)
        logger.debug("set inol for {0} rep(s) @ {1} is {2}".format(str(r), str(intensity), str(set_inol)))
        for s in range(min_sets, max_sets + 1):
            exercise_inol = set_inol * s
            volume = r * s
            weight = current_max * (float(intensity) / 100)
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

