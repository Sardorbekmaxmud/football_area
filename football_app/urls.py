from django.urls import path
from .views import *

urlpatterns = [
    path('', AllStadiumView.as_view()),
]