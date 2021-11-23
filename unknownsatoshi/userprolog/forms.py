from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    name = forms.CharField(max_length=50, required=True)
    phone = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=255, required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['email'].widget.attrs.update({
            'class': 'input-field',
            'required':'',
            'name':'email',
            'id':'email',
            'type':'email',
            'placeholder':'Email Address',
            })
        self.fields['username'].widget.attrs.update({
            'class': 'input-field',
            'required':'',
            'name':'username',
            'id':'username',
            'type':'text',
            'placeholder':'Username',
            'maxlength': '16',
            'minlength': '6',
            })
        self.fields['phone'].widget.attrs.update({
            'class': 'input-field',
            'required':'',
            'name':'phone',
            'id':'phone',
            'type':'tel',
            'placeholder':'Phone number',
            'maxlength': '16',
            'minlength': '6',
            })
        self.fields['password1'].widget.attrs.update({
            'class': 'input-field',
            'required':'',
            'name':'password1',
            'id':'password1',
            'type':'password',
            'placeholder':'Enter password',
            'maxlength': '22',
            'minlength': '8',
            })
        self.fields['password2'].widget.attrs.update({
            'class': 'input-field',
            'required':'',
            'name':'password2',
            'id':'password2',
            'type':'password',
            'placeholder':'Confirm your password',
            'maxlength': '22',
            'minlength': '8',
            })
        self.fields['name'].widget.attrs.update({
            'class': 'input-field',
            'required':'',
            'name':'name',
            'id':'name',
            'type':'text',
            'placeholder':'Your name',

            })  


    class Meta:
        model = User
        fields = ['username','name','email', 'phone', 'password1', 'password2']    