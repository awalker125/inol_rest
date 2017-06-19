# from . import api, ns
# from .models import inolRequest, inolResponse
# from flask import render_template
# from flask_restplus import Resource

# 
# 
# 
# @ns.route('/<int:reps>')
# @api.doc(params={'reps': 'rep count'})
# class Inol(Resource):
# 
#     @api.marshal_with(inolRequest)
#     def get(self, reps):
#         '''Fetch a given resource'''
#         inolResponse = inolResponse(resp=reps, weight=100.0, max=105.00, inol=0.8)
#         return inolResponse
# 
# @ns.app_errorhandler(403)
# def forbidden(e):
#     return render_template('403.html'), 403
# 
# 
# @ns.app_errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html'), 404
# 
# 
# @ns.app_errorhandler(500)
# def internal_server_error(e):
#     return render_template('500.html'), 500
# 
# 


