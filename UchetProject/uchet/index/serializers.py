from rest_framework import serializers
from .models import Departments,Technics,Cheludi, UserProfile

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
        
class UserPorfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""  
    class Meta:
        model = UserProfile
        fields = ('id','email','name','password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style':{'input_type': 'password'}
            }
        }

    def create(self,validated_data):
        """Create and return a new user"""
        user = UserProfile.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password']
        )

        return user