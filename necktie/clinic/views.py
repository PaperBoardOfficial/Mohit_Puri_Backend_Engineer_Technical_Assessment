from rest_framework import generics
from .models import Clinic
from .serializers import ClinicSerializer

class ClinicListView(generics.ListAPIView):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer