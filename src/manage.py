#! /usr/bin/env python

import os

from inol_rest import create_app

from flask_script import Manager


app = create_app(os.getenv('INOL_REST_ENV') or 'dev')
manager = Manager(app)




if __name__ == '__main__':
    manager.run()
