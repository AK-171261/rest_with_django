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


# get_resources(1)

def create_resource():
    new_emp = {
        "ename": 'kanika',
        "eno": 600,
        "esal": 7000,
        "eaddr": 'Hyderabad',
    }

    resp = requests.post(BASE_URL + ENDPOINT, data=json.dumps(new_emp))
    print(resp.status_code)
    print(resp.json())


# create_resource()

def update_resource(id):
    new_emp = {
        "id": id,
        'ename':'Kanika Chugh',
        "esal": 120000,
    }

    resp = requests.put(BASE_URL + ENDPOINT, data=json.dumps(new_emp))
    print(resp.status_code)
    print(resp.json())


id = input("Enter id: ")
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

