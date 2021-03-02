from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from .utils import is_json
from .mixins import HttpResponseMixin, SerializeMixin
from .models import Student
from django.views.decorators.csrf import csrf_exempt  # to disable csrf_token
from django.utils.decorators import method_decorator  # to disable csrf_token at class level
from .forms import StudentForm
import json


@method_decorator(csrf_exempt, name="dispatch")
class StudentCRUDCBV(HttpResponseMixin, SerializeMixin, View):
    def get_object_by_id(self, id):
        try:
            student = Student.objects.get(id=id)
        except Student.DoesNotExist:
            student = None
        return student

    def get(self, request, *args, **kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            return self.render_to_http_response(json.dumps({"msg": "Please provide valid json data only"}), status=400)
        pdata = json.loads(data)
        id = pdata.get('id', None)
        if id is not None:
            student_object = self.get_object_by_id(id)
            if student_object is None:
                return self.render_to_http_response(
                    json.dumps({"msg": "No matched record found with corresponding id!"}),
                    status=400)
            json_data = self.serialize([student_object])
            return self.render_to_http_response(json_data)
        student_obj = Student.objects.all()
        json_data = self.serialize(student_obj)
        return self.render_to_http_response(json_data)

    def post(self, request, *args, **kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            return self.render_to_http_response(json.dumps({"msg": "Please provide valid json data only"}), status=400)
        student_data = json.loads(data)
        form = StudentForm(student_data)
        if form.is_valid():
            form.save(commit=True)
            return self.render_to_http_response(json.dumps({'msg': 'Data saved sucessfully'}))
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_http_response(json_data, status=400)

    def put(self, request, *args, **kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            return self.render_to_http_response(json.dumps({"msg": "Please provide valid json data only"}), status=400)
        provided_data = json.loads(data)
        id = provided_data.get('id', None)
        if id is not None:
            student_object = self.get_object_by_id(id)
            if student_object is None:
                return self.render_to_http_response(
                    json.dumps({"msg": "No matched record found with corresponding id!"}),
                    status=400)
            original_data = {
                "name": student_object.name,
                "rollno": student_object.rollno,
                "marks": student_object.marks,
                "gf": student_object.gf,
                "bf": student_object.bf,
            }
            original_data.update(provided_data)
            form = StudentForm(original_data, instance=student_object)
            if form.is_valid():
                form.save(commit=True)
                return self.render_to_http_response(json.dumps({'msg': 'Resource updatedsucessfully'}))
            if form.errors:
                json_data = json.dumps(form.errors)
                return self.render_to_http_response(json_data, status=400)
        return self.render_to_http_response(json.dumps({"msg": "Id is required to perform Updation"}), status=400)

    def delete(self, request, *args, **kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({"msg": "Please send valid json data only"})
            return self.render_to_http_response(json_data, status=400)
        pdata = json.loads(data)
        id = pdata.get('id', None)
        if id is not None:
            emp = self.get_object_by_id(id)
            if emp is None:
                json_data = json.dumps({"msg": "The requested resource not available"})
                return self.render_to_http_response(json_data, status=400)
            status, deleted_item = emp.delete()
            if status == 1:
                json_data = json.dumps({"msg": "Resource deleted Sucessfully"})
                return self.render_to_http_response(json_data)
            json_data = json.dumps({"msg": "unable to delete"})
            return self.render_to_http_response(json_data)
        json_data = json.dumps({"msg": "To perform deletion id is mandatory,please provide."})
        return self.render_to_http_response(json_data)
