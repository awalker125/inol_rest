#import os
from flask import url_for
from flask_testing import TestCase
import sys
import logging
import json

import inol_rest
#from thermos.models import User, Bookmark


logger = logging.getLogger()
logger.level = logging.DEBUG
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)

class InolRestTestCase(TestCase):

    def create_app(self):
        logger.debug("creating app")
        return inol_rest.create_app('test')

    def setUp(self):
        logger.debug("setting up client")
        self.client = self.app.test_client()

        #u = User(username='test', email='test@example.com', password='test')

        #self.client.post(url_for('auth.login'),
        #    data = dict(username='test', password='test'))

#    def tearDown(self):



    def test_200OK_when_sending_valid_inol_request(self):
        
        request_data =   dict(
                            max = 100.00,
                            reps = 10,
                            weight = 70
                            ) 
        
        response = self.client.post(
            url_for('api.set_inol'),
            data=json.dumps(request_data),
            content_type='application/json',
            follow_redirects = True
            )
        logger.debug("response.status_code {0}".format(response.status_code))
        
        assert response.status_code == 200
    
    def test_200OK_and_correct_inol_when_sending_valid_inol_request(self):
        
        request_data =   dict(
                            max = 100.00,
                            reps = 2,
                            weight = 80.00
                            ) 
        
        response = self.client.post(
            url_for('api.set_inol'),
            data=json.dumps(request_data),
            content_type='application/json',
            follow_redirects = True
            )
        logger.debug("response.status_code {0}".format(response.status_code))
        logger.debug("response.data {0}".format(response.data))
        
        response_data = json.loads(response.data)
        assert response.status_code == 200
        assert response_data['inol'] == 0.1

    def test_400BADREQUEST_when_sending_inol_request_with_missing_data(self):
        
        request_data =   dict(
                            max = 100.00,
                            reps = 2
                            ) 
        
        response = self.client.post(
            url_for('api.set_inol'),
            data=json.dumps(request_data),
            content_type='application/json',
            follow_redirects = True
            )
        logger.debug("response.status_code {0}".format(response.status_code))
        logger.debug("response.data {0}".format(response.data))
        
        response_data = json.loads(response.data)
        assert response.status_code == 400     