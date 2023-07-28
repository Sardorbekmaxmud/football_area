from django.shortcuts import render
from rest_framework import generics
from .models import StadiumModel
from .serializers import StadiumSerializer
from rest_framework.permissions import IsAuthenticated


# Create your views here.


class AllStadiumView(generics.ListAPIView):
    queryset = StadiumModel.objects.all()
    serializer_class = StadiumSerializer
    # permission_classes = (IsAuthenticated, )
