from rest_framework import serializers
from .models import Employee

# serializer class

class EmployeeSerializer(serializers.ModelSerializer):
    class  Meta:
       model = Employee
       fields = '__all__'
    