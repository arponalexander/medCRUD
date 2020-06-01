from django.db import models


class Medication_R01(models.Model):

    medication_route_rec = models.CharField(max_length=200)
    route = models.CharField(max_length=200)
    abbreviation = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Medication R01'

    def __str__(self):
        return self.medication_route_rec


class Medication_R02(models.Model):
    medication_frequency_rec = models.CharField(max_length=200)
    frequency = models.CharField(max_length=200)
    abbreviation = models.ForeignKey(Medication_R01, on_delete=models.CASCADE, max_length=200, null=True)

    class Meta:
        verbose_name = 'Medication R02'

    def __str__(self):
        return self.medication_frequency_rec


class Medication_B00(models.Model):
    medication_rec = models.CharField(max_length=200)
    patient_rec = models.CharField(max_length=200)
    medication_type = models.CharField(max_length=200)
    medication = models.CharField(max_length=200)
    medication_route_rec = models.ForeignKey(Medication_R01, max_length=200, on_delete=models.CASCADE, null=True)
    medication_frequency_rec = models.ForeignKey(Medication_R02, max_length=200, on_delete=models.CASCADE, null=True)
    prescribed_by = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    active_status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Medication B00'

    def __str__(self):
        return self.medication_rec
