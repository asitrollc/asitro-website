from flask import Flask, request, render_template , jsonify, redirect, url_for, Blueprint
errors = Blueprint('errors', __name__, template_folder='templates',static_folder='static')



@errors.app_errorhandler(400)
def error(e):
    return render_template('errors/404.html'), 400
@errors.app_errorhandler(401)
def error(e):
    return render_template('errors/401.html'), 401
@errors.app_errorhandler(403)
def error(e):
    return render_template('errors/403.html'), 403
@errors.app_errorhandler(404)
def error(e):
    return render_template('errors/404.html'), 404
@errors.app_errorhandler(500)
def error(e):
    return render_template('errors/500.html'), 500
@errors.app_errorhandler(503)
def error(e):
    return render_template('errors/503.html'), 503
@errors.app_errorhandler(504)
def error(e):
    return render_template('errors/504.html'), 504
  