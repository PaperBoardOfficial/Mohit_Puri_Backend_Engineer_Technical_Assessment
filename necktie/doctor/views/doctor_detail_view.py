from rest_framework import generics

from doctor.models import Doctor
from doctor.serializers import DoctorSerializer


class DoctorDetailView(generics.RetrieveAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
