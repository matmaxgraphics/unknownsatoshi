from django import forms
from .models import User


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_no', 'email', 'username', 'profile_picture', 'is_active', 'is_staff', 'is_superuser']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class':"input-field"})
        self.fields['last_name'].widget.attrs.update({'class':"input-field"})
        self.fields['phone_no'].widget.attrs.update({'class':"input-field"})
        self.fields['email'].widget.attrs.update({'class':"input-field"})
        self.fields['username'].widget.attrs.update({'class':"input-field"})
        self.fields['profile_picture'].widget.attrs.update({'class':"input-field"})
        self.fields['is_active'].widget.attrs.update({'class':"input"})
        self.fields['is_staff'].widget.attrs.update({'class':"input"})
        self.fields['is_superuser'].widget.attrs.update({'class':"input"})
