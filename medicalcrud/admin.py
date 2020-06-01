from django.contrib import admin
from .models import Medication_B00, Medication_R01, Medication_R02


class CRUDAdmin(admin.ModelAdmin):
    list_display = ['medication_Rec']


class CRUDAdmin2(admin.ModelAdmin):
    list_display = ['medication_Route_Rec']


class CRUDAdmin3(admin.ModelAdmin):
    list_display = ['medication_Frequency_Rec']


admin.site.register(Medication_B00, CRUDAdmin)
admin.site.register(Medication_R01, CRUDAdmin2)
admin.site.register(Medication_R02, CRUDAdmin3)
