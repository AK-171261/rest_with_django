# # Create your tests here.
import requests

#
# #
BASE_URL = "http://localhost:8000/"
ENDPOINT = "api/"


#
def get_resource(id):
    resp = requests.get(BASE_URL + ENDPOINT + id + '/')
    # if resp.status_code in range(200,300):
    # if resp.status_code == requests.codes.ok:
    print(resp)
    print(resp.status_code)
    print(resp.json())
    # else:
    #     print("something goes wrong")


id = input("Enter id: ")
# get_resource(id)
#
# # import requests
# #
# # BASE_URL = "http://localhost:8000/"
# # ENDPOINT = "apilist/"
# #
# # def get_resource():
# #     resp = requests.get(BASE_URL+ENDPOINT)
# #     print(resp.status_code)
# #     print(resp.json())
# #
# # get_resource()
#
# # import requests
# #
# # BASE_URL = "http://localhost:8000/"
# # ENDPOINT = "apilist/"
# #
# # def get_all():
# #     resp = requests.get(BASE_URL+ENDPOINT)
# #     print(resp.status_code)
# #     print(resp.json())
# #
# # get_all()
import json

#
BASE_URL = "http://localhost:8000/"
ENDPOINT = "apilist/"


def create_resource():
    new_emp = {
        'eno': 1,
        'ename': 'shiva',
        'esal': 10000,
        'eaddr': 'mizoram',
    }
    resp = requests.post(BASE_URL + ENDPOINT, data=json.dumps(new_emp))
    print(resp.status_code)
    print(resp.json())


# create_resource()

BASE_URL = "http://localhost:8000/"
ENDPOINT = "api/"


def update_resource(id):
    new_emp = {
        'esal': 10000,
        'eaddr': 'mizoram',
    }
    resp = requests.put(BASE_URL + ENDPOINT + str(id) + '/', data=json.dumps(new_emp))
    print(resp.status_code)
    print(resp.json())


# update_resource(7)

def delete_resource(id):
    resp = requests.delete(BASE_URL + ENDPOINT + str(id) + '/')
    print(resp.status_code)
    print(resp.json())


# delete_resource(6)

# with single end point
BASE_URL = "http://localhost:8000/"
ENDPOINT = "apilistttt/"


def CRUD_with_single_endpoint_(id=None):
    data = {}
    if id is not None:
        data = {
            'id': id
        }
    resp = requests.get(BASE_URL + ENDPOINT, data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())

CRUD_with_single_endpoint_(2)