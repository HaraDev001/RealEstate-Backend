from rest_framework import serializers
from .models import Realtors

class RealtorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realtors
        fields = '__all__'
