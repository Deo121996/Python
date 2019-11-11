import json


from flask import Flask, make_response, request
from simple_mongo import insert_data, fetch_data

DATABASE = 'tea'
COLLECTION = 'cups'

app = Flask(__name__)
# data = [{'id':1, 'name':'tanya'}, {'id':2, 'name':'subratho'}, {'id':3, 'name':'utkarsh'}, {'id':12, 'name':'Anand'}]




@app.route("/get_name/", methods=['GET', 'POST', 'PUT'])
def print_route():
    if request.method == 'GET':

        data = fetch_data(DATABASE, COLLECTION,{})

        # print(request.args)
        # name = request.args.get('name')
        # for user in data:
        #     if user['id'] == int(id) and user['name'] == name:
        #         resp = user
        #         return make_response(json.dumps(resp),200)
        # return make_response(json.dumps(resp),404)

        return make_response(json.dumps(data),400)


    if request.method == 'POST':
        print("FORMDATA")
        print(request.form)
        print("HEADERS")
        print(request.headers.get('requested'))
        print("BODY")
        print(request.get_json())
        print("PARAMETERS")
        print(request.args)



        data = insert_data(DATABASE, COLLECTION, dict(request.get_json()))
        return make_response("Successfull",200)

    if request.method == 'PUT':
        name = request.args.get('name')
        print(name)
        new = request.get_json()
        for user in data:
            if user['name'] == name:
                user['name'] = new['name']
                return make_response(json.dumps(data),200)
        return make_response(json.dumps({}),404)


if __name__ == '__main__':
   app.run(debug = True)


