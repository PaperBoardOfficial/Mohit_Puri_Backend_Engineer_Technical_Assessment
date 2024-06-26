from rest_framework import generics
from doctor.models import Doctor
from doctor.serializers import DoctorSerializer
from doctor.filters import DoctorFilter
from django_filters.rest_framework import DjangoFilterBackend

class DoctorListCreateView(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    filterset_class = DoctorFilter
    filter_backends = [DjangoFilterBackend]