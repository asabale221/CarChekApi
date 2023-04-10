from rest_framework import serializers

from apps.cars.models import Car, SpecialMarks, PeriodsOwnership

class SpecialMarksSerializers(serializers.ModelSerializer):
    class Meta:
        model = SpecialMarks
        fields ="__all__"
        
class PeriodsOwnershipSerializers(serializers.ModelSerializer):
    class Meta:
        model = PeriodsOwnership
        fields ="__all__"

class CarSerializers(serializers.ModelSerializer):
    cars_special_marks = SpecialMarksSerializers(read_only=True, many=True)
    cars_periods_ownership = PeriodsOwnershipSerializers(read_only=True, many=True)
    class Meta:
        model = Car
        fields = ('id', 'license_plate', 'brand', 'model', 
                'engine_volume',
                'cars_special_marks', 'cars_periods_ownership')