from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import RegisterView

app_name = "users"

urlpatterns = [

    path("sinup/", RegisterView.as_view(), name="register"),
    #path("login/", LoginView.as_view(), name="login"),
    #path("logout/", LogoutView.as_view, name="logout")
]
