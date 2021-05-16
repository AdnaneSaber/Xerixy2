from .models import PhoneClick
from rest_framework import serializers

class PhoneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PhoneClick
        fields = ["__all__"]