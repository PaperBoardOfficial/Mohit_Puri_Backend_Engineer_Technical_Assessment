from rest_framework import serializers

from doctor.models import ConsultationDetail

class ConsultationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultationDetail
        fields = ('inclusive', 'days', 'consultation_fee', 'member_exclusive_price')
