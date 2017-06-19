from flask import render_template

from . import home




@home.route('/')
def index():
    return render_template('index.html', google_analytics_tracking_id="UA-101246577-1")


@home.app_errorhandler(403)
def forbidden(e):
    return render_template('403.html'), 403


@home.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@home.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500




