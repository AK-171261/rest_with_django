# Create your tests here.
import requests
#
BASE_URL = "http://localhost:8000/"
ENDPOINT = "api/"

def get_resource(id):
    resp = requests.get(BASE_URL+ENDPOINT+id+'/')
    # if resp.status_code in range(200,300):
    # if resp.status_code == requests.codes.ok:
    print(resp)
    print(resp.status_code)
    print(resp.json())
    # else:
    #     print("something goes wrong")

id = input("Enter id: ")
get_resource(id)

# import requests
#
# BASE_URL = "http://localhost:8000/"
# ENDPOINT = "apilist/"
#
# def get_resource():
#     resp = requests.get(BASE_URL+ENDPOINT)
#     print(resp.status_code)
#     print(resp.json())
#
# get_resource()

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
