from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class SelectRoom(LoginRequiredMixin, TemplateView):
    template_name = 'room/index.html'
    login_url = reverse_lazy('login')


class RoomView(LoginRequiredMixin, TemplateView):
    template_name = 'room/room.html'
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['room_name'] = kwargs['room']
        return context