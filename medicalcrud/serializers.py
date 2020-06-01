from rest_framework import serializers
from .models import Medication_R01, Medication_B00, Medication_R02


class Medication_R01_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Medication_R01
        fields = '__all__'


class Medication_R02_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Medication_R02
        fields = '__all__'


class Medication_B00_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Medication_B00
        fields = '__all__'
