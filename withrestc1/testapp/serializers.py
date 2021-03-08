from rest_framework import serializers
from .models import Employee


def multiple_of_1000(value):
    if value % 1000 != 0:
        raise serializers.ValidationError("Employee salary should multiples of 1000")


class EmployeeSerializer(serializers.ModelSerializer):
    esal = serializers.FloatField(validators=[multiple_of_1000])

    class Meta:
        model = Employee
        fields = '__all__'
# class EmployeeSerializer(serializers.Serializer):
#     eno = serializers.IntegerField()
#     ename = serializers.CharField(max_length=64)
#     esal = serializers.FloatField(validators=[multiple_of_1000])
#     eaddr = serializers.CharField(max_length=64)
#
#     def create(self, validated_data):
#         return Employee.objects.create(**validated_data)
#
#     # Field level validation
#     def validate_esal(self, data):
#         print(data)
#         if data <= 5000:
#             raise serializers.ValidationError('Employee salary should be minimum 5000')
#         return data
#
#     # object level validation
#     def validate(self, attrs):
#         ename = attrs.get('ename')
#         esal = attrs.get('esal')
#         if ename.lower() == 'sunny':
#             if esal < 50000:
#                 raise serializers.ValidationError('Sunny salary should be 50000')
#         return attrs
#
#     def update(self, instance, validated_data):
#         instance.eno = validated_data.get('eno', instance.eno)
#         instance.ename = validated_data.get('ename', instance.ename)
#         instance.esal = validated_data.get('esal', instance.esal)
#         instance.eaddr = validated_data.get('eaddr', instance.eaddr)
#         instance.save()
#         return instance
