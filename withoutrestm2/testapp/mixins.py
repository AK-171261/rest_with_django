from django.core.serializers import serialize
from django.http import HttpResponse
import json


class SerializeMixin(object):
    def serialize(self, qs ):
        json_data = serialize('json', qs) #json_data = serialize('json', qs, fields=('eno','ename','esal))
        p_dict = json.loads(json_data)
        lst = []
        for obj in p_dict:
            lst.append(obj["fields"])
        json_data = json.dumps(lst)
        return json_data


class HttpResponseMixin(object):
    def render_to_http_response(self, json_data, status=200):
        return HttpResponse(json_data, content_type="application/json", status=status)
