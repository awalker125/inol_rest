#! /usr/bin/env python

import os

from inol_rest import create_app

from flask_script import Server, Manager


app = create_app(os.getenv('INOL_REST_ENV') or 'dev')

server = Server(host="0.0.0.0")



manager = Manager(app)

manager.add_command("runserver", server)


if __name__ == '__main__':
    manager.run()
