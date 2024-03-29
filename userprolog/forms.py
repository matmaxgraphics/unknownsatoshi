from django import forms
from .models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, PasswordResetForm



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email',)

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email',)

    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)


class UserUpdateForm(forms.ModelForm):
    profile_picture = forms.ImageField(required=False, error_messages={'required':"An image is required"})
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


class MyPasswordResetForm(PasswordResetForm):
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is not registered.")
        return email