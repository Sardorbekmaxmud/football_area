from rest_framework import serializers
from .models import StadiumModel


class StadiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = StadiumModel
        fields = ('id', 'address', 'contact', 'images', 'price', 'started_at', 'end_at', )
