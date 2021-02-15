# Create your tests here.
import requests

# BASE_URL = "http://localhost:8000/"
# ENDPOINT = "api/"
#
# def get_resource(id):
#     resp = requests.get(BASE_URL+ENDPOINT+id+'/')
#     print(resp.status_code)
#     print(resp.json())
# id = input("Enter id: ")
# get_resource(id)

import requests

BASE_URL = "http://localhost:8000/"
ENDPOINT = "apilist/"

def get_resource():
    resp = requests.get(BASE_URL+ENDPOINT)
    print(resp.status_code)
    print(resp.json())

get_resource()

# import requests
#
# BASE_URL = "http://localhost:8000/"
# ENDPOINT = "api/"
#
# def get_all():
#     resp = requests.get(BASE_URL+ENDPOINT)
#     print(resp.status_code)
#     print(resp.json())
#
# get_all()
