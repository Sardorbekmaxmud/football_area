from rest_framework.serializers import ModelSerializer
from .models import StadiumModel,BronModel

class StadiumSerializer(ModelSerializer):
    class Meta:
        model = StadiumModel
        fields = '__all__'

class BronSerializer(ModelSerializer):
    class Meta:
        model = BronModel
        fields = '__all__'
