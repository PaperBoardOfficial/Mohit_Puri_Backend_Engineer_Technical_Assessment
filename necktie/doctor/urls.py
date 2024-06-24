from django.urls import path
from .views import DoctorListCreateView, DoctorDetailView

urlpatterns = [
    path('doctor/', DoctorListCreateView.as_view(), name='doctor-list-create'),
    path('doctor/<int:pk>/', DoctorDetailView.as_view(), name='doctor-detail'),
]