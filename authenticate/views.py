from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.urls import reverse_lazy

from authenticate.forms import UserForm

class CustomLoginView(LoginView):
    template_name = "auth/login.html"
    next_page = reverse_lazy("select_room")


class UserCreateView(CreateView):
    form_class = UserForm
    success_url = reverse_lazy("login")
    template_name = "auth/register.html"

