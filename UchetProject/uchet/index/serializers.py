from rest_framework import serializers
from .models import Departments,Technics,Cheludi

class DepartmentsSerializer(serializers.ModelSerializer):
    """Serializer для списка отделов"""

    class Meta:
        model = Departments
        fields = '__all__'

    def create(self, validated_data):
        """"""
        department = Departments.objects.create(
            name = validated_data['name'],
            address = validated_data['address']
        )
        return department

class TechnicsSerializer(serializers.ModelSerializer):
    """Serializer для списка техники"""

    class Meta:
        model = Technics
        fields = '__all__'
        
class CheludiSerializer(serializers.ModelSerializer):
    """Serializer для списка людей"""

    class Meta:
        model = Cheludi
        fields = '__all__'
        