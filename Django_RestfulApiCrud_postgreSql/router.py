from employeeApi.viewsets import EmployeeViewset
from rest_framework import routers

# setting up the router function



router = routers.DefaultRouter()
router.register('employee',EmployeeViewset)

