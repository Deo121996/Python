
from flask import Flask
from flask_restplus import Api, Resource, fields, Namespace
app = Flask(__name__)
ns_v2 = Namespace('New API', description='New APIs')


todo = ns_v2.model('New API', {
    'id': fields.Integer(readOnly=True, description='The task unique identifier'),
    'task': fields.String(required=True, description='The task details')
})


class TodoDAO(object):
    def __init__(self):
        self.counter = 0
        self.todos = []

    def get(self, id):
        for todo in self.todos:
            if todo['id'] == id:
                return todo
        ns_v2.abort(404, "Todo {} doesn't exist".format(id))

    def create(self, data):
        todo = data
        todo['id'] = self.counter = self.counter + 1
        self.todos.append(todo)
        return todo

    def update(self, id, data):
        todo = self.get(id)
        todo.update(data)
        return todo

    def delete(self, id):
        todo = self.get(id)
        self.todos.remove(todo)


DAO = TodoDAO()

@ns_v2.route('/')
class TodoList(Resource):
    '''Shows a list of all todos, and lets you POST to add new tasks'''
    @ns_v2.doc('list_todos')
    @ns_v2.marshal_list_with(todo)
    def get(self):
        '''List all tasks'''
        return DAO.todos

    @ns_v2.doc('create_todo')
    @ns_v2.expect(todo)
    @ns_v2.marshal_with(todo, code=201)
    def post(self):
        '''Create a new task'''
        return DAO.create(ns_v2.payload), 201


@ns_v2.route('/<int:id>')
@ns_v2.response(404, 'Todo not found')
@ns_v2.param('id', 'The task identifier')
class Todo(Resource):
    '''Show a single todo item and lets you delete them'''
    @ns_v2.doc('get_todo')
    @ns_v2.marshal_with(todo)
    def get(self, id):
        '''Fetch a given resource'''
        return DAO.get(id)

    @ns_v2.doc('delete_todo')
    @ns_v2.response(204, 'Todo deleted')
    def delete(self, id):
        '''Delete a task given its identifier'''
        DAO.delete(id)
        return '', 204

    @ns_v2.expect(todo)
    @ns_v2.marshal_with(todo)
    def put(self, id):
        '''Update a task given its identifier'''
        return DAO.update(id, ns_v2.payload)



# NO_WHITESPACE_REGEX = "^[^-\s].*$"
# NO_WHITESPACE_SPECIALCHAR_REGEXP = "^([^\!\^\&\`\s\:\/\\\[\]\:\;\|\=\,\*\?\<\>])+$"
# NO_SPECIAL_CHAR_ALLOW_UNDERSCORE="^([a-zA-Z0-9_]*)$"
