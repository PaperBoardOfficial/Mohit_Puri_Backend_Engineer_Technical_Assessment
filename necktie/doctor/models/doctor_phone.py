from django.db import models

from doctor.models import Doctor

class DoctorPhone(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f'{self.doctor.name} - {self.phone}'