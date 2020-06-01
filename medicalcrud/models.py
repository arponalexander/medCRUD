from django.db import models


class Medication_R01(models.Model):

    medication_Route_Rec = models.CharField(max_length=200)
    route = models.CharField(max_length=200)
    abbreviation = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Medication R01'

    def __str__(self):
        return self.medication_Route_Rec


class Medication_R02(models.Model):
    medication_Frequency_Rec = models.CharField(max_length=200)
    frequency = models.CharField(max_length=200)
    abbreviation = models.ForeignKey(Medication_R01, on_delete=models.DO_NOTHING, max_length=200)

    class Meta:
        verbose_name = 'Medication R02'

    def __str__(self):
        return self.medication_Frequency_Rec


class Medication_B00(models.Model):
    medication_Rec = models.CharField(max_length=200)
    patient_Rec = models.CharField(max_length=200)
    medication_Type = models.CharField(max_length=200)
    medication = models.CharField(max_length=200)
    medication_Route_Rec = models.ForeignKey(Medication_R01, max_length=200, on_delete=models.DO_NOTHING)
    medication_Frequency_Rec = models.ForeignKey(Medication_R02, max_length=200, on_delete=models.DO_NOTHING)
    prescribed_By = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    active_Status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Medication B00'

    def __str__(self):
        return self.medication_Rec
