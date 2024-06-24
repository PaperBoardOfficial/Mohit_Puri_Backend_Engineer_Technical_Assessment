from django.contrib import admin
from .models import ConsultationDetail, Doctor, Schedule, DoctorPhone

admin.site.register(ConsultationDetail)
admin.site.register(Doctor)
admin.site.register(Schedule)
admin.site.register(DoctorPhone)
