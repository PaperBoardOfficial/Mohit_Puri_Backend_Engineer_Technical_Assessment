import django_filters
from .models import Doctor


class DoctorFilter(django_filters.FilterSet):
    price_min = django_filters.NumberFilter(
        field_name="consultation_detail__consultation_fee", lookup_expr="gte"
    )
    price_max = django_filters.NumberFilter(
        field_name="consultation_detail__consultation_fee", lookup_expr="lte"
    )
    district = django_filters.CharFilter(
        field_name="clinic__district", lookup_expr="exact"
    )


    class Meta:
        model = Doctor
        fields = [
            "speciality",
            "language",
            "price_min",
            "price_max",
            "district",
        ]
