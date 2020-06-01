from django.urls import path,include
from . import views
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register('Medication_R01', views.MedicationR01View)
routers.register('Medication_R02', views.MedicationR02View)
routers.register('Medication_B00', views.MedicationB00View)

urlpatterns = [
    path('', include(routers.urls))
]
