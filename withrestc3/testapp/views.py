from django.shortcuts import render
from rest_framework.views import APIView
from testapp.models import Employee
from .serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework.generics import ListAPIView


# class EmployeeListAPIView(APIView):
#     def get(self, request, format=None):
#         qs = Employee.objects.all()
#         serializer = EmployeeSerializer(qs, many=True)
#         return Response(serializer.data)


class EmployeeListAPIView(ListAPIView):
    import pdb
    pdb.set_trace()
    get_queryset = Employee.objects.all()
    queryset = EmployeeSerializer

