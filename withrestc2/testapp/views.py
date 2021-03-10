from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from testapp.serializers import NameSerializer


class TestAPIView(APIView):
    def get(self, request, *args, **kwargs):
        colors = ["RED", "YELLOW", "GREEN", "BLUE"]
        return Response({'msg': 'Happy Pongal', 'colors': colors})

    def post(self, request, *args, **kwargs):
        serializer = NameSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            msg = "Hello {},Happy Pongal!!!".format(name)
            return Response({"msg": msg})
        else:
            return Response(serializer.errors, status=400)

    def put(self, request, *args, **kwargs):
        return Response({"msg": "This is response from put method"})

    def patch(self, request, *args, **kwargs):
        return Response({"msg": "This is response from patch method"})

    def delete(self, request, *args, **kwargs):
        return Response({"msg": "This is response from delete method"})


from rest_framework.viewsets import ViewSet


class TestViewSet(ViewSet):
    def list(self, request):
        colors = ["RED", "YELLOW", "GREEN", "BLUE"]
        return Response({'msg': 'Happy new year', 'colors': colors})

    def create(self, request):
        serializer = NameSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            msg = "Hello {},Happy Pongal!!!".format(name)
            return Response({"msg": msg})
        else:
            return Response(serializer.errors, status=400)

    def retrive(self, request, *args, **kwargs):
        return Response({"msg": "This is response from retrive method"})

    def update(self, request, *args, **kwargs):
        return Response({"msg": "This is response from update method"})

    def partial_update(self, request, *args, **kwargs):
        return Response({"msg": "This is response from partial_update method"})

    def destroy(self, request, *args, **kwargs):
        return Response({"msg": "This is response from delete method"})
