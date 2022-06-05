from flask_restful import Resource
from flask import Flask, jsonify
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
class keepalive(Resource):
    def get(self):
      return jsonify({"Time": current_time,
             "Endpoint": "Ping / keep alive"})
    def post(self):
      return {"Error": "We dont support post requests for this endpoint"}
    def delete(self):
      return {"Error": "We dont support post requests for this endpoint"}      