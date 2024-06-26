from rest_framework import generics

from doctor.models import Doctor
from doctor.serializers import DoctorSerializer
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator


class DoctorDetailView(generics.RetrieveAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    @method_decorator(cache_page(60*15)) # Cache for 15 minutes
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)