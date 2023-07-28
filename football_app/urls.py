from django.urls import path
from .views import BronsView,DeleteBron,StadiumDetailUserView,StadiumBronUserView

urlpatterns = [
    # owner api
    path('bron/<str:bron_status>/',BronsView.as_view()),
    path('bron/<pk>/',DeleteBron.as_view()),

    # user api
    path('bron/',StadiumBronUserView.as_view()),
    path('<pk>/',StadiumDetailUserView.as_view()),
]