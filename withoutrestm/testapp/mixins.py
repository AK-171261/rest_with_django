from django.core.serializers import serialize
import json


class SerializeMixin(object):
    def serialize(self, qs):
        json_data = serialize('json', qs)
        p_dict = json.loads(json_data)
        lst = []
        for obj in p_dict:
            lst.append(obj["fields"])
        json_data = json.dumps(lst)
        return json_data
