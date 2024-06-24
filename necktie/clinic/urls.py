from django.urls import path
from .views import ClinicListView

urlpatterns = [
    path('clinic/', ClinicListView.as_view(), name='clinic-list'),
]