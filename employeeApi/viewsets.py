from rest_framework import viewsets,filters
from . import models
from . import serializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

class EmployeeViewset(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializer.EmployeeSerializer
    # filter_backends = [DjangoFilterBackend, SearchFilter]
    # filterset_fields = ['fullname',]


    def get_queryset(self):
        queryset = super().get_queryset()
        id = self.request.query_params.get('id', None)
        fullname = self.request.query_params.get('fullname', None)

        if id:
            # Filter by ID if 'id' parameter is provided
            queryset = queryset.filter(id=id)

        if fullname:
            # Filter by full name if 'fullname' parameter is provided
            queryset = queryset.filter(fullname__icontains=fullname)

        return queryset

