from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register(prefix='employees', viewset=views.EmployeeViewSet, basename='employees')

urlpatterns = router.urls