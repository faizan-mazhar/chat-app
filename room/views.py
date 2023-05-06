import json
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from room.forms import ChatRoomForm
from room.models import ChatRoom, Message

class SelectRoomView(LoginRequiredMixin, CreateView):
    template_name = 'room/index.html'
    login_url = reverse_lazy('login')
    form_class = ChatRoomForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["rooms"] = ChatRoom.objects.all()
        return context
    
    def get_success_url(self):
        return reverse('chat_room', args=[self.object.name])


class RoomView(LoginRequiredMixin, TemplateView):
    template_name = 'room/room.html'
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        room_name = kwargs['room']
        context['room_name'] =room_name
        context['messages'] = json.dumps([
            {"message": message.message, "id": message.sender} for message in Message.objects.filter(room__name=room_name)]
            )
        return context