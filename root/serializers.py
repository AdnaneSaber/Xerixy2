from .models import phoneClick
from rest_framework import serializers

class PhoneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = phoneClick
        fields = ["__all__"]