from django.shortcuts import render
from django.views.generic import View
from .models import Employee
import json
from django.http import HttpResponse
from .mixins import SerializeMixin, HttpResponseMixin
from django.views.decorators.csrf import csrf_exempt  # to disable csrf_token
from django.utils.decorators import method_decorator  # to disable csrf_token at class level
from testapp.utils import is_json
from .forms import EmployeeForm
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

# using serializers
from django.core.serializers import serialize


class EmployeeDetailCBV(HttpResponseMixin, SerializeMixin, View):
    def get(self, request, id, *args, **kwargs):
        try:
            emp = Employee.objects.get(id=id)  # we got emp object from that object we will fetch desired result
        except Employee.DoesNotExist:
            json_data = json.dumps({"msg": "The requested resource is not available"})
            # return HttpResponse(json_data, content_type='application/json', status=404)
            return self.render_to_http_response(json_data, status=404)
        # emp_data = {
        #     'eno': emp.eno,
        #     'ename': emp.ename,
        #     'esal': emp.esal,
        #     'eaddr': emp.eaddr,
        # }
        # json_data = json.dumps(emp_data)
        # json_data = serialize('json', [emp, ], fields=['ename', 'esal'])
        else:
            json_data = self.serialize([emp])
            # return HttpResponse(json_data, content_type='application/json', status=200)
            return self.render_to_http_response(json_data)


@method_decorator(csrf_exempt, name="dispatch")
class EmployeeListCBV(HttpResponseMixin, SerializeMixin, View):
    def get(self, request, *args, **kwargs):
        emp = Employee.objects.all()  # we got emp object from that object we will fetch desired result
        # json_data = serialize('json', emp, fields=('esal','eno'))
        # p_dict = json.loads(json_data)
        # lst = []
        # for obj in p_dict:
        #     lst.append(obj["fields"])
        # json_data = json.dumps(lst)
        json_data = self.serialize(emp)
        return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        # json_data = json.dumps({"msg": "This is from post"})
        # print(request)
        # return self.render_to_http_response(json_data=json_data)
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({"msg": "Please send valid json data only"})
            return self.render_to_http_response(json_data, status=400)
        # json_data = json.dumps({"msg": "valid json data only"})
        # return self.render_to_http_response(json_data)
        emp_data = json.loads(data)
        form = EmployeeForm(emp_data)
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({"msg": "Resource is created sucessfully"})
            return self.render_to_http_response(json_data)
        if form.errors:
            json_data = json.dumps(form.errors)  # form.errors is dictonary only
            return self.render_to_http_response(json_data, status=400)
