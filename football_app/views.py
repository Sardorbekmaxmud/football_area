from django.shortcuts import render,get_object_or_404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import StadiumModel,BronModel
from .serializers import StadiumSerializer,BronSerializer
from config.permissions import OwnerPermission
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class BronsView(APIView):
    def get(self,request,*args,**kwargs):
        try:
            print(kwargs["bron_status"])
            all_bron = BronModel.objects.filter(bron_status=kwargs["bron_status"].title())
            serializer = BronSerializer(all_bron,many=True)
            permission_classes = (OwnerPermission,)
            return Response(serializer.data)
        except:
            return Response({"message":"please enter true value only"})

class DeleteBron(generics.DestroyAPIView):
    queryset = BronModel.objects.all()
    serializer_class = BronSerializer
    permission_classes = (OwnerPermission,)

# ----------------- user views ----------------------------
class StadiumDetailUserView(generics.RetrieveAPIView):
    queryset = StadiumModel.objects.all()
    serializer_class = StadiumSerializer
    permission_classes = (IsAuthenticated,)

class StadiumBronUserView(generics.CreateAPIView):
    queryset = BronModel.objects.all()
    serializer_class = BronSerializer
    permission_classes = (IsAuthenticated,)

class AllStadiumView(generics.ListAPIView):
    queryset = StadiumModel.objects.all()
    serializer_class = StadiumSerializer
    # permission_classes = (IsAuthenticated, )
