from django import forms
from room.models import ChatRoom


class ChatRoomForm(forms.ModelForm):

    class Meta:
        model = ChatRoom
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
        }
