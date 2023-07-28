from django.urls import path
from .views import user_signup, UserUpdate

urlpatterns = [
    path('signup/', user_signup, name='user_signup'),
    path('crud_user/<pk>/', UserUpdate.as_view())
]