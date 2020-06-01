from django.urls import path,include
from . import views
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register('medication_r01', views.MedicationR01View)
routers.register('medication_r02', views.MedicationR02View)
routers.register('medication_b00', views.MedicationB00View)

urlpatterns = [
    path('', include(routers.urls))
]
