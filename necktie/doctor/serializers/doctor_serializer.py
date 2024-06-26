from typing import List, Dict, Any
from rest_framework import serializers
from clinic.serializers import ClinicSerializer
from doctor.serializers import ConsultationDetailSerializer, ScheduleSerializer
from doctor.models import ConsultationDetail, Schedule, Doctor
from clinic.models import Clinic
from doctor.models import DoctorPhone
from doctor.serializers import DoctorPhoneSerializer

class DoctorSerializer(serializers.ModelSerializer):
    clinic = ClinicSerializer()
    consultation_detail = ConsultationDetailSerializer()
    schedule = serializers.SerializerMethodField()
    phone = serializers.SerializerMethodField()
    
    class Meta:
        model = Doctor
        fields = "__all__"

    def get_schedule(self, obj: Doctor) -> List[Dict[str, Any]]:
        schedule = Schedule.objects.filter(doctor=obj)
        return ScheduleSerializer(schedule, many=True).data

    def get_phone(self, obj: Doctor) -> List[str]:
        phone = DoctorPhone.objects.filter(doctor=obj)
        return [phone.phone for phone in phone]

    def create(self, validated_data: Dict[str, Any]) -> Doctor:
        consultation_detail_data = validated_data.pop("consultation_detail")
        consultation_detail = ConsultationDetail.objects.create(**consultation_detail_data)
        clinic_data = validated_data.pop("clinic")
        clinic = Clinic.objects.create(**clinic_data)
        doctor = Doctor.objects.create(consultation_detail=consultation_detail, clinic=clinic, **validated_data)
        phone_data = self.initial_data.get('phone', [])
        for phone_entry in phone_data:
            phone_serializer = DoctorPhoneSerializer(data={'phone': phone_entry})
            if phone_serializer.is_valid(raise_exception=True):
                DoctorPhone.objects.create(doctor=doctor, phone=phone_entry)
        schedule_data = self.initial_data.get("schedule", [])
        for schedule_entry in schedule_data:
            schedule_serializer = ScheduleSerializer(data=schedule_entry)
            if schedule_serializer.is_valid(raise_exception=True):
                Schedule.objects.create(doctor=doctor, **schedule_serializer.validated_data)
    
        return doctor