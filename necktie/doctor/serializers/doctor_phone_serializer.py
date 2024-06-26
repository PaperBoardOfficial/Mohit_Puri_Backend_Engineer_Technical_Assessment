from rest_framework import serializers
from doctor.models import DoctorPhone
from django.core.validators import RegexValidator

class DoctorPhoneSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])

    class Meta:
        model = DoctorPhone
        fields = ['phone']