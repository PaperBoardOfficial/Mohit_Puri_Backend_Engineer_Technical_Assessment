from rest_framework import generics
from rest_framework.exceptions import APIException

from doctor.serializers import DoctorQuerySerializer
from .models import Doctor
from .serializers import DoctorSerializer
from rest_framework.exceptions import ValidationError


class DoctorListCreateView(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    def get_queryset(self):
        try:
            queryset = super().get_queryset()
            serializer = DoctorQuerySerializer(data=self.request.query_params)
            if serializer.is_valid():
                district = self.request.query_params.get("district")
                speciality = self.request.query_params.get("speciality")
                price_min = self.request.query_params.get("price_min")
                price_max = self.request.query_params.get("price_max")
                language = self.request.query_params.get("language")

                if district:
                    queryset = queryset.filter(clinic__district=district)
                if speciality:
                    queryset = queryset.filter(speciality=speciality)
                if price_min and price_max:
                    queryset = queryset.filter(
                        consultation_detail__consultation_fee__range=(
                            price_min,
                            price_max,
                        )
                    )
                elif price_min:
                    queryset = queryset.filter(
                        consultation_detail__consultation_fee__gte=price_min
                    )
                elif price_max:
                    queryset = queryset.filter(
                        consultation_detail__consultation_fee__lte=price_max
                    )
                if language:
                    queryset = queryset.filter(language=language)

                return queryset
            else:
                raise ValidationError(serializer.errors)
        except Exception as e:
            raise APIException(detail=str(e))


class DoctorDetailView(generics.RetrieveAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
