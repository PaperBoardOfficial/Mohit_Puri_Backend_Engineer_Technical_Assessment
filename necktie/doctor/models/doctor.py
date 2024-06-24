from django.db import models

from clinic.models import Clinic
from doctor.models import ConsultationDetail


class Doctor(models.Model):
    LANGUAGE_CHOICES = [
        ("English", "English"),
        ("Cantonese", "Cantonese"),
        ("Mandarin", "Mandarin"),
    ]
    name = models.CharField(max_length=255)
    speciality = models.CharField(max_length=255)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    consultation_detail = models.ForeignKey(ConsultationDetail, on_delete=models.CASCADE)
    language = models.CharField(max_length=100, choices=LANGUAGE_CHOICES, default="english")

    def __str__(self):
        return self.name
