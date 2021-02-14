from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def emp_data_view(request):
    emp_data = {
        "eno": 100,
        "ename": "Anand",
        "esal": 1000,
        "eaddress": 100,

    }
    resp = '<h1>Employee Number:{}<br>Employee Name:{}<br>Employee Salary:{}<br>Employee Address:{}</h1>'.format(
        emp_data["eno"],
        emp_data["ename"],
        emp_data["esal"],
        emp_data["eaddress"])
    return HttpResponse(resp)


import json


# python support


def emp_data_json_view(request):
    emp_data = {
        "eno": 100,
        "ename": "Anand",
        "esal": 1000,
        "eaddress": 100,

    }
    return HttpResponse(json.dumps(emp_data),
                        content_type="application/json")  # MIME type multi purpose internet mail extension


from django.http import JsonResponse


# Django Suppport


def emp_data_json_view2(request):
    emp_data = {
        "eno": 100,
        "ename": "Anand",
        "esal": 1000,
        "eaddress": 100,

    }
    return JsonResponse(emp_data)


from django.views.generic import View
from testapp.mixins import AnandResponseMixin

# class JsonCBV(View):
#     def get(self, request, *args, **kwargs):
#         emp_data = {
#             "eno": 100,
#             "ename": "Anand",
#             "esal": 1000,
#             "eaddress": 100,
#
#         }
#         return JsonResponse(emp_data)


# class JsonCBV(View):
#     def get(self, request, *args, **kwargs):
#         json_data = json.dumps({"msg": "This is get method"})
#         return HttpResponse(json_data, content_type="application/json")
#
#     def post(self, request, *args, **kwargs):
#         json_data = json.dumps({"msg": "This is post method"})
#         return HttpResponse(json_data, content_type="application/json")
#
#     def put(self, request, *args, **kwargs):
#         json_data = json.dumps({"msg": "This is put method"})
#         return HttpResponse(json_data, content_type="application/json")
#
#     def delete(self, request, *args, **kwargs):
#         json_data = json.dumps({"msg": "This is delete method"})
#         return HttpResponse(json_data, content_type="application/json")
#
#

#using mixin to remove duplication and maintain code reusability
class JsonCBV(AnandResponseMixin, View):
    def get(self, request, *args, **kwargs):
        json_data = json.dumps({"msg": "This is get method"})
        return self.render_to_http_response(json_data)

    def post(self, request, *args, **kwargs):
        json_data = json.dumps({"msg": "This is post method"})
        return self.render_to_http_response(json_data)

    def put(self, request, *args, **kwargs):
        json_data = json.dumps({"msg": "This is put method"})
        return self.render_to_http_response(json_data)

    def delete(self, request, *args, **kwargs):
        json_data = json.dumps({"msg": "This is delete method"})
        return self.render_to_http_response(json_data)
