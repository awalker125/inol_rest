#!/bin/bash

curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' -d '{ "min_set_inol": 0.05, "intensity": 80, "min_exercise_inol": 0.3, "max_exercise_inol": 2, "maximum": 182.5, "max_sets": 6, "max_reps": 12, "max_set_inol": 0.5 }' 'http://walandre9:5000/api/training/options'
