'''
Created on 20 May 2017

@author: walandre
'''
from __future__ import division
import math
import logging


logger = logging.getLogger(__name__)


#Lombardi
def lomrm(reps, weight):
    return math.floor(weight * (math.pow(reps, 0.10)))

#Brzycki                      
def brzrm(reps, weight):
    return  math.floor(weight * 36 / (37 - reps))
    
#Epley
def eplrm(reps,  weight):
    return math.floor(weight * ((1 + (reps / 30))))


#Mayhew
def mayrm(reps, weight):
    return  math.floor((100 * weight) / ( 52.2 + 41.9 * math.exp(-0.055*reps)))

# o'conner
def ocorm(reps, weight):
    return math.floor(weight  * (1 + reps / 40))

#Wathan
def watrm(reps, weight):
    return math.floor(weight * 100 / (48.8 + 53.8 * math.exp( -0.075 * reps)))


#Lander
def lanrm(reps, weight):
    return math.floor((100 * weight) / (101.3 - (2.67123 * reps))) 

#average
def avgrm(reps,weight):
    
    lomrm_result = lomrm(reps,weight)
    brzrm_result = brzrm(reps,weight)
    eplrm_result = eplrm(reps,weight)
    mayrm_result = mayrm(reps,weight)
    ocorm_result = ocorm(reps,weight)
    watrm_result = watrm(reps,weight)
    lanrm_result = lanrm(reps,weight)
    
    return math.floor((lomrm_result + brzrm_result + eplrm_result + mayrm_result + ocorm_result + watrm_result + lanrm_result )/7)


def calculate_excercise_inol(reps, weight, current_max, sets):
    
    return calculate_set_inol(reps, weight, current_max) * sets
    
def calculate_set_inol(reps, weight, current_max):
    if (weight > current_max):
        logger.warning("weight {0} > max {1}. Will set theoretical max to be weight + 0.5".format(str(weight),str(current_max)))
        current_max = weight + 0.5
    elif (weight == current_max):
        logger.warning("weight {0} = max {1}. Will set theoretical max to be weight + 0.5".format(str(weight),str(current_max)))
        current_max = weight + 0.5
   
    intensity = (weight / current_max) * 100
    logger.debug("intensity {0}".format(str(intensity)))

    return  calculate_inol(reps,intensity)    
    
def calculate_inol(reps, intensity):
    
    if (intensity == 100):
        intensity = intensity - 0.01 # we'll make it 99.9 %
    
    return reps / (100 - intensity )
#    return reps / (100 - (intensity + math.pow(0,intensity))





if __name__ == '__main__':
    pass