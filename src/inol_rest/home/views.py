from flask import render_template
from flask import current_app

from inol_rest.home import home
import datetime

@home.app_errorhandler(403)
def forbidden(e):
    return render_template('403.html'), 403


@home.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@home.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


def base_properties():
    base = {}
    
    year = datetime.datetime.now().year
    application_domain_name = current_app.config['APPLICATION_DOMAIN_NAME']
    application_name = current_app.config['APPLICATION_NAME']
    google_analytics_tracking_id = current_app.config['GOOGLE_ANALYTICS_TRACKING_ID']
    
    base['year'] = year
    base['application_domain_name'] = application_domain_name
    base['application_name'] = application_name
    base['google_analytics_tracking_id'] = google_analytics_tracking_id

    
    return base
    


@home.route('/')
def index():
    #base = base_properties()
    
    
    return render_template('index.html', base_properties=base_properties())



@home.route('inol')
def inol():
    
    return render_template('inol.html', base_properties=base_properties)



