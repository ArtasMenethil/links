from django import forms
from .models import UsersLink


class LinkFromUser(forms.ModelForm):
    class Meta:
        model = UsersLink
        fields = ['link_url', 'link']
        widgets = {
            'link': forms.TextInput(attrs={'class': 'form-input'}),
            'link_url': forms.TextInput(attrs={'class': 'form-input'}),
            'user': forms.HiddenInput()
        }
