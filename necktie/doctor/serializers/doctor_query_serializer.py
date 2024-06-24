from rest_framework import serializers


class DoctorQuerySerializer(serializers.Serializer):
    district = serializers.CharField(required=False)
    speciality = serializers.CharField(required=False)
    price_min = serializers.IntegerField(required=False, min_value=0)
    price_max = serializers.IntegerField(required=False, min_value=0)
    language = serializers.CharField(required=False)

    def validate(self, data):
        if "price_min" in data and "price_max" in data:
            if data["price_min"] > data["price_max"]:
                raise serializers.ValidationError(
                    "price_min cannot be greater than price_max"
                )
        return data
