from rest_framework import viewsets,status
from .models import Employee
from rest_framework.response import Response
from . import serializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

class EmployeeViewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = serializer.EmployeeSerializer
    # filter_backends = [DjangoFilterBackend, SearchFilter]
    # filterset_fields = ['fullname',]


    def get_object(self):
        param = self.kwargs.get('fullname')  # Get the URL parameter (fullname or id)

        try:
            if param.isdigit():
                # If the parameter is a digit, assume it's an ID
                return Employee.objects.get(id=param)
            else:
                # Otherwise, assume it's a fullname
                return Employee.objects.get(fullname=param)
        except Employee.DoesNotExist:
            return Response(
                {"detail": "Employee not found."},
                status=status.HTTP_404_NOT_FOUND
            )

