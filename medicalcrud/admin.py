from django.contrib import admin
from .models import Medication_B00, Medication_R01, Medication_R02


class CRUDAdmin(admin.ModelAdmin):
    list_display = ['medication_rec']


class CRUDAdmin2(admin.ModelAdmin):
    list_display = ['medication_route_rec']


class CRUDAdmin3(admin.ModelAdmin):
    list_display = ['medication_frequency_rec']


admin.site.register(Medication_B00, CRUDAdmin)
admin.site.register(Medication_R01, CRUDAdmin2)
admin.site.register(Medication_R02, CRUDAdmin3)
