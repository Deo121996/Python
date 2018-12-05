from flask import Flask
from flask_restplus import Api, Resource

app = Flask(__name__)

api = Api(app,version=1.0,title="Simple Session API", description="simple apis")

ns = api.namespace('Session',description='a smiple session')
@ns.route('/')
class Sessionlist(Resource):

def get(self):
    return []


