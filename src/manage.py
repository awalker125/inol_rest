#! /usr/bin/env python

import os

from inol_rest import create_app
from flask import url_for
from flask_script import Server, Manager


app = create_app(os.getenv('INOL_REST_ENV') or 'dev')

server = Server(host="0.0.0.0")



manager = Manager(app)

manager.add_command("runserver", server)


@manager.command
def list_routes():
    import urllib
    output = []
    for rule in app.url_map.iter_rules():

        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)

        methods = ','.join(rule.methods)
        url = url_for(rule.endpoint, **options)
        line = urllib.unquote("{:50s} {:20s} {}".format(rule.endpoint, methods, url))
        output.append(line)
    
    for line in sorted(output):
        print line


if __name__ == '__main__':
    manager.run()
