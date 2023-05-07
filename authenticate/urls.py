# chat/urls.py
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from authenticate.views import CustomLoginView, UserCreateView


urlpatterns = [
    path("login/", CustomLoginView.as_view() , name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", UserCreateView.as_view(), name="register"),
    path("api/v1/", include("authenticate.api.v1.urls")),
]