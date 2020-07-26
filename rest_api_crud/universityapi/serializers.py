from rest_framework import serializers
from .models import Univeristy

class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Univeristy
        fields = '__all__'