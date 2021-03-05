from django.shortcuts import render
from django.views.generic import View
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .serializers import EmployeeSerializer
from .models import Employee
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import io


@method_decorator(csrf_exempt, name='dispatch')
class EmployeeCRUDCBV(View):
    def get(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pdata = JSONParser().parse(stream)
        id = pdata.get('id', None)
        if id is not None:
            emp = Employee.objects.get(id=id)
            eserializer = EmployeeSerializer(emp)
            json_data = JSONRenderer().render(eserializer.data)
            return HttpResponse(json_data, content_type='application/json', status=200)
        emp = Employee.objects.all()
        eserializer = EmployeeSerializer(emp, many=True)
        json_data = JSONRenderer().render(eserializer.data)
        return HttpResponse(json_data, content_type='application/json', status=200)

    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pdata = JSONParser().parse(stream)
        serializer = EmployeeSerializer(data=pdata)
        if serializer.is_valid():
            serializer.save()
            msg = {"msg": "Resource created successfully"}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type="application/json", status=200)
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type="application/json", status=400)

    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pdata = JSONParser().parse(stream)
        id = pdata.get('id')
        emp = Employee.objects.get(id=id)
        serializer = EmployeeSerializer(emp, data=pdata, partial=True)
        if serializer.is_valid():
            serializer.save()
            msg = {"msg": "Resource Updated successfully"}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type="application/json", status=200)
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type="application/json", status=400)

    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pdata = JSONParser().parse(stream)
        id = pdata.get('id')
        emp = Employee.objects.get(id=id)
        emp.delete()
        msg = {"msg": "Resource Deleted successfully"}
        json_data = JSONRenderer().render(msg)
        return HttpResponse(json_data, content_type="application/json", status=200)
