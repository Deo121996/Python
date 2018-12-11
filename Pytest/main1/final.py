from flask import Flask
from flask_restplus import Api, Resource, fields
import logging
from new_module import ns_v2


app = Flask(__name__)

api = Api(app, version='1.0', title='Session API',
          description='A simple Session API',
          )

ns = api.namespace('sessions', description='Session Operations')

api.add_namespace(ns_v2,path='/todos')


session = api.model('Session Input', {
    'session': fields.String(required=True, description='name of session'),
    'presenter': fields.String(required=True, description='presenter of session', enum=['Dev', 'Omkar', 'Ashish'])
})

sessionOp = api.model('Session Output', {
    'id': fields.Integer(readOnly=True, description='The session unique identifier'),
    'session': fields.String(required=True, description='The session details'),
    'presenter': fields.String(required=True, description='The session presenter')
})


def create_logger_module(module_name):
    logger_format = '%(asctime)s %(levelname)-2s [%(filename)s:%(lineno)d] %(message)s'
    logging.basicConfig(format=logger_format, datefmt='%d-%m-%Y:%H:%M:%S',
                        level=logging.INFO)
    logger = logging.getLogger(module_name)
    return logger


logger = create_logger_module("Flask-rest-plus")


class SessionDAO(object):
    def __init__(self):
        self.counter = 0
        self.sessions = []

    def get(self, id):
        for session in self.sessions:
            if session['id'] == id:
                return session
     

    def create(self, data, id=0):
        session = data
        if not session:
            return None
        if not id:
            self.counter = self.counter+1
            id = self.counter

        session['id'] = id
        session['extra'] = "extra"
        self.sessions.append(session)
        # logger.info("Creted Sessions"+session)
        return session

    def update(self, id, data):
        session = self.get(id)
        session.update(data)
        return session

    def delete(self, id):
        session = self.get(id)
        self.sessions.remove(session)


DAO = SessionDAO()


@ns.route('/')
class Sessionlist(Resource):
    def validate_payload(self, func):
        return super(Sessionlist, self).validate_payload(func)

    '''Shows a list of all sessions, and lets you POST to add new session'''

    @ns.marshal_list_with(sessionOp)
    @ns.doc('list_sessions')
    def get(self):
        '''List all session'''
        return DAO.sessions

    # @ns.marshal_with(sessionOp, code=201)

    @ns.doc('create_session')
    @ns.expect(session, validate=True)
    def post(self):
        '''Create a new session'''
        return DAO.create(api.payload), 201


@ns.route('/<int:id>')
@ns.response(404, 'Session not found')
@ns.param('id', 'The Session identifier')
class Session(Resource):
    '''Show a single Session item and lets you delete them'''
    @ns.doc('get_session_by_id')
    @ns.marshal_with(sessionOp)
    def get(self, id):
        '''Fetch a given resource'''
        return DAO.get(id), 200

    @ns.doc('delete_session')
    @ns.response(204, 'Session deleted')
    def delete(self, id):
        '''Delete a session given its identifier'''
        DAO.delete(id)
        return '', 204

    @ns.expect(session)
    @ns.marshal_with(sessionOp)
    def put(self, id):
        '''Update a session given its identifier'''
        return DAO.update(id, api.payload), 200
