from rest_framework import viewsets,filters
from . import models
from . import serializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

class EmployeeViewset(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializer.EmployeeSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['fullname',]