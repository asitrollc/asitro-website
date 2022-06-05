from flask import Flask, request, render_template , jsonify, redirect, url_for, Blueprint
leagal = Blueprint('leagal', __name__, template_folder='templates',static_folder='static')

@leagal.route('/privacy')
def privacy():
  return render_template('leagal/privacy.html')

@leagal.route('/tos')
def tos():
  return render_template('leagal/tos.html')

@leagal.route('/copyright')
def copyright():
  return render_template('leagal/copyright.html')