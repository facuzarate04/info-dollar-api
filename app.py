from flask import Flask
from flask_restful import Resource, Api
import script
import json

app = Flask("Info Dollar")
api = Api(app)


class DollarOficial(Resource):
    def get(self, value: str):
        if value == "all":
            response = script.dollar_oficial()
            return json.dumps(response)
        response = script.dollar_oficial()
        if value in response:
            return json.dumps(response[value])
        pass

class DollarBlue(Resource):
    def get(self, value: str):
        if value == "all":
            response = script.dollar_blue()
            return json.dumps(response)
        response = script.dollar_blue()
        if value in response:
            return json.dumps(response[value])
        pass
        

api.add_resource(DollarOficial, '/oficial/<string:value>')
api.add_resource(DollarBlue, '/blue/<string:value>')


if __name__ == '__main__':
    app.run(debug=True)

