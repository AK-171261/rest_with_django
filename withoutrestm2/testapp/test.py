import requests
import json

BASE_URL = "http://localhost:8000/"
ENDPOINT = "api/"


def get_resources(id=None):
    data = {}
    if id is not None:
        data = {
            'id': id
        }
    resp = requests.get(BASE_URL + ENDPOINT, data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())


get_resources()

def create_resource():
    new_emp = {
        "name": 'Virat',
        "rollno": 106,
        "marks": 35,
        "gf": 'Anushka',
        "bf": 'Dhoni'
    }

    resp = requests.post(BASE_URL + ENDPOINT, data=json.dumps(new_emp))
    print(resp.status_code)
    print(resp.json())


# create_resource()

def update_resource(id):
    new_emp = {
        "id": id,
        "marks": 300,
        "gf": 'Twinkle'
    }

    resp = requests.put(BASE_URL + ENDPOINT, data=json.dumps(new_emp))
    print(resp.status_code)
    print(resp.json())


# id = input("Enter id: ")
# update_resource(id)


def delete_resource(id=None):
    data = {}
    if id is not None:
        data = {
            'id': id
        }
    resp = requests.delete(BASE_URL + ENDPOINT, data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())


# delete_resource(id)
