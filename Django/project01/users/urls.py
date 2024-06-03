from django.urls import path
from . import views

urlpatterns = [
    path('', views.Users.as_view()),
    path('<int:user_id>/addresses', views.UserAddress.as_view()),
]