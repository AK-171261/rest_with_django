from django.shortcuts import render
from rest_framework.views import APIView
from testapp.models import Employee
from .serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework.generics import (ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView,
                                     ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework import mixins
from rest_framework import generics


# class EmployeeListAPIView(APIView):
#     def get(self, request, format=None):
#         qs = Employee.objects.all()
#         serializer = EmployeeSerializer(qs, many=True)
#         return Response(serializer.data)


# class EmployeeListAPIView(ListAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#
#     def get_queryset(self):
#         qs = Employee.objects.all()
#         name = self.request.GET.get('ename')
#         if name is not None:
#             qs = qs.filter(ename__icontains=name)
#         return qs
#
#
# class EmployeeCreateAPIView(CreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#
#
# class EmployeeRetrieveAPIView (RetrieveAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     lookup_field = 'id'
#
#
# class EmployeeUpdateAPIView(UpdateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     lookup_field = 'id'
#
#
# class EmployeeDestroyAPIView(DestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     lookup_field = 'id'


class EmployeeListCreateAPIView(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        qs = Employee.objects.all()
        name = self.request.GET.get('ename')
        if name is not None:
            qs = qs.filter(ename__icontains=name)
        return qs


class EmployeeRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'id'


class EmployeeRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'id'


class EmployeeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'id'


class EmployeeListCreateModelMixin(generics.ListAPIView, mixins.CreateModelMixin):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    # def list(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class EmployeeRetrieveUpdateDestroyModelMixin(generics.RetrieveAPIView, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'id'

    # def list(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(self, request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(self, request, *args, **kwargs)
