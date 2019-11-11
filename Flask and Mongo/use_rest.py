import requests
import json

#POST request
resp = requests.post("http://127.0.0.1:5000/get_name/",data=json.dumps({'id':234,'name':'renu'}), headers={'requested':'Raees', 'Content-Type':'application/json'})
print("POST response body")
print(resp.text)
print("POST status code")
print(resp.status_code)

#GET REQUEST
resp = requests.get("http://127.0.0.1:5000/get_name/")
print("GET response body")
print(resp.text)
print("GET status code")
print(resp.status_code)
