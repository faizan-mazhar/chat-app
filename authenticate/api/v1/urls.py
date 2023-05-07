from django.urls import path
from authenticate.api.v1.viewsets import LoginAPIView

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name="api_login")
]