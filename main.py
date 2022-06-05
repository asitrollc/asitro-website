from flask import Flask, request, render_template , jsonify, redirect, url_for
from flask_restful import Resource, Api
from blueprints.backend.database.tests.test import Data
import pymongo
from blueprints.public_routes.msic import msic
from blueprints.backend.redirects.redirect import main_redirect
from utilities.database.database_setup import *
from blueprints.public_routes.main import main
from blueprints.devloper_routes.testing.test import tests
from blueprints.error_handlers.error_handler import errors
from blueprints.public_routes.leagal import leagal
from blueprints.backend.api.heath.keepalive import keepalive
# google translate link
#https://luficer--website-rjmanhas-repl-co.translate.goog/?_x_tr_sl=fr&_x_tr_tl=en&_x_tr_hl=en&_x_tr_pto=wapp


#restfull
#https://flask-restful.readthedocs.io/en/latest/quickstart.html#resourceful-routing


#google
#https://translate.google.com/translate?sl=fr&tl=en&hl=en&u=https://luficer-website.rjmanhas.repl.co//db/insert/data/&client=webapp


app = Flask(__name__,
            static_url_path='/static',
            static_folder='static')
api = Api(app)
app.register_blueprint(msic)
app.register_blueprint(main_redirect)
app.register_blueprint(errors)
app.register_blueprint(main)
app.register_blueprint(tests)
app.register_blueprint(leagal)







api.add_resource(Data, '/db/insert/<string:ip>/')
api.add_resource(keepalive, '/backend/api/heath/check/ping/')

app.run(host='0.0.0.0', port=81, debug=True)