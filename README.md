inol_rest
========================


## building
	cd inol_rest/src/inol_rest/static
	gulp

## running locally
	cd inol_rest/
	. ./setup_shell.sh
	cd src
	./manage.py runserver


This is a microservice responsible for doing all of the inol calculations


curl
-----------------------------
	curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' --header 'X-Fields: inol' -d '{ \ 
	"max": 100, \ 
	"reps": 1, \ 
	"weight": 100 \ 
	}' 'http://127.0.0.1:5000/api/inol/'