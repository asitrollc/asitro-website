from flask_restful import Resource


class Data(Resource):
    def get(self, ip):
        print("data")
        return{"type": "data", "Ip": ip}
    def post(self):
      return {"Error": "We dont support post requests for this endpoint"}
    def delete(self):
      return {"Error": "We dont support post requests for this endpoint"}      