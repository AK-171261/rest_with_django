from django.shortcuts import render
from django.views.generic import View
from .models import Employee
import json
from django.http import HttpResponse


# Create your views here.

# class EmployeeDetailCBV(View):
#     def get(self, request, *args, **kwargs):
#         emp = Employee.objects.get(id=3)  # we got emp object from that object we will fetch desired result
#         emp_data = {
#             'eno': emp.eno,
#             'ename': emp.ename,
#             'esal': emp.esal,
#             'eaddr': emp.eaddr,
#         }
#         json_data = json.dumps(emp_data)
#         return HttpResponse(json_data, content_type='application/json')

# to dynamically pass the id
# class EmployeeDetailCBV(View):
#     def get(self, request, id, *args, **kwargs):
#         emp = Employee.objects.get(id=id)  # we got emp object from that object we will fetch desired result
#         emp_data = {
#             'eno': emp.eno,
#             'ename': emp.ename,
#             'esal': emp.esal,
#             'eaddr': emp.eaddr,
#         }
#         json_data = json.dumps(emp_data)
#         return HttpResponse(json_data, content_type='application/json')

#using serializers
from django.core.serializers import serialize


class EmployeeDetailCBV(View):
    def get(self, request, id, *args, **kwargs):
        emp = Employee.objects.get(id=id)  # we got emp object from that object we will fetch desired result
        # emp_data = {
        #     'eno': emp.eno,
        #     'ename': emp.ename,
        #     'esal': emp.esal,
        #     'eaddr': emp.eaddr,
        # }
        # json_data = json.dumps(emp_data)
        json_data = serialize('json',[emp,],fields=['ename','esal'])
        return HttpResponse(json_data, content_type='application/json')


class EmployeeListCBV(View):
    def get(self, request, *args, **kwargs):
        emp = Employee.objects.all()  # we got emp object from that object we will fetch desired result
        json_data = serialize('json', emp,fields=['esal'])
        p_dict = json.loads(json_data)
        lst=[]
        for obj in p_dict:
            lst.append(obj["fields"])
        json_data = serialize('json',lst)
        return HttpResponse(json_data, content_type='application/json')
