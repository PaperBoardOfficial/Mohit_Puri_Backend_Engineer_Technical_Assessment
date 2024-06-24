from rest_framework import serializers
from doctor.models import Schedule

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ('day_of_week', 'start_time', 'end_time')
        
    def validate_day(self, value):
        valid_days = [day[0] for day in Schedule.DAYS_OF_WEEK]
        if value not in valid_days:
            raise serializers.ValidationError("Invalid day of the week.")
        return value