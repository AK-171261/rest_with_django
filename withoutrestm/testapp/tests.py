from django.test import TestCase

# Create your tests here.
# import requests
#
# BASE_URL = "http://localhost:8000/"
# ENDPOINT = "apilist/"
#
# # def get_resource(id):
# #     resp = requests.get(BASE_URL+ENDPOINT+id+'/')
# #     print(resp.status_code)
# #     print(resp.json())
# # id = input("Enter id: ")
# # get_resource(id)
#
# # import requests
# #
# # BASE_URL = "http://localhost:8000/"
# # ENDPOINT = "api/"
# #
# # def get_resource():
# #     resp = requests.get(BASE_URL+ENDPOINT)
# #     print(resp.status_code)
# #     print(resp.json())
# #
# # get_resource()
#
# import requests
#
# BASE_URL = "http://localhost:8000/"
# ENDPOINT = "apilist/"
#
# def get_all():
#     resp = requests.get(BASE_URL+ENDPOINT)
#     print(resp.status_code)
#     print(resp.json())
#
# get_all()

# class A:
#     def get_nm(self):
#         return "hi"
#
#
# class B():
#     def get_nm(self):
#         return "hello"
#
#
# class C(A,B):
#     def get_nm(self):
#         return super(C, self).get_nm()
#
#
# print(C.mro())
# class A:
#
#     def __init__(self):
#         self.name="Rajesh"
#
#     def test(self):
#         print("Hello from A")
#
#
# class B(A):
#
#     def __init__(self):
#         #super()._init_()
#         self.name="Rajesh"
#
#     def test(self):
#         super(B, self).test()
#
# class C(B):
#
#     def __init__(self):
#         #super().__init__()
#         self.name="Rajesh"
#
#     def test(self):
#         super(C, self).test()
# obj=C()
# obj.test()

arr = [1,0,2,0,3,4,0,0,6,0]
count=0
for i in range(len(arr)):
    if arr[i] != 0:
        arr[count]=arr[i]
        count+=1
while count<len(arr):
    arr[count]=0
    count+=1

print(arr)