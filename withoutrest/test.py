import requests

BASE_URL = "http://localhost:8000/"
ENTRY_POINT = "apijsoncbv/"
resp = requests.post(BASE_URL + ENTRY_POINT)
print(resp.text)
