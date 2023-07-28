from rest_framework import serializers
from .models import StadiumModel


class StadiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = StadiumModel
        fields = ('name', 'address', 'contact', 'images', 'price', 'started_at', 'end_at', )