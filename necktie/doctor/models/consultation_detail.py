from django.db import models


class ConsultationDetail(models.Model):
    inclusive = models.BooleanField(default=False)
    days = models.PositiveIntegerField(null=True, blank=True)
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2)
    member_exclusive_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )

    def __str__(self):
        return f"Consultation Details (ID: {self.id})"
