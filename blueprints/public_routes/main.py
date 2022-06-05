from flask import Flask, request, render_template , jsonify, redirect, url_for, Blueprint
main = Blueprint('main', __name__, template_folder='templates',static_folder='static')

@main.route('/')
def index():
  # return redirect(url_for('msic.test'))
  botinfo = {'servers': 1000, 
             'users': 1250, 
             'commands': 10}
  return render_template('main/index.html', server_count=botinfo['servers'], users_count=botinfo['users'], command_count=botinfo['commands'])