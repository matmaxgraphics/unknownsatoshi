from userprolog.models import User
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

from ckeditor_uploader.widgets import CKEditorUploadingWidget




class CmsForm(forms.ModelForm):
    
    class Meta:
        model = Cms
        fields = ['title', 'entry', 'stoploss', 'tp_target', 'tp_achieved', 'profit', 'featured_image', 'tags']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({"class": "input-field"})
        self.fields['entry'].widget.attrs.update({'class': "input-field"})
        self.fields['stoploss'].widget.attrs.update({'class': "input-field"})
        self.fields['tp_target'].widget.attrs.update({'class': "input-field"})
        self.fields['tp_achieved'].widget.attrs.update({'class': "input-field"})
        self.fields['profit'].widget.attrs.update({'class': "input-field"})
        self.fields['tags'].widget.attrs.update({'class': "input-field"})
        self.fields['featured_image'].widget.attrs.update({'class': "input-field"})

        

        
class BlogForm(forms.ModelForm):
    post = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Blog
        fields = ['title', 'post', 'featured_image','featured_stories','latest_news','latest_articles']
        exclude = ['author']
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({'class': "input-field"})
        self.fields['post'].widget.attrs.update({})
        self.fields['featured_image'].widget.attrs.update({'class': "input-field"})
        self.fields['featured_stories'].widget.attrs.update({})
        self.fields['latest_news'].widget.attrs.update({})
        self.fields['latest_articles'].widget.attrs.update({})


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['courses', 'course_link', 'featured_image', ]
        
    
    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        self.fields['courses'].widget.attrs.update({'class':"input-field"})
        self.fields['course_link'].widget.attrs.update({'class':"input-field"})
        self.fields['featured_image'].widget.attrs.update({'class':"input-field"})

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'product_link','price', 'featured_image', 'tags']
        
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product_name'].widget.attrs.update({'class':"input-field"})
        self.fields['product_link'].widget.attrs.update({'class':"input-field"})
        self.fields['price'].widget.attrs.update({'class':"input-field"})
        self.fields['featured_image'].widget.attrs.update({'class':"input-field"})
        self.fields['tags'].widget.attrs.update({'class':"input-field"})


class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'product_link','price', 'featured_image', 'tags']
        
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product_name'].widget.attrs.update({'class':"input-field"})
        self.fields['product_link'].widget.attrs.update({'class':"input-field"})
        self.fields['price'].widget.attrs.update({'class':"input-field"})
        self.fields['featured_image'].widget.attrs.update({'class':"input-field"})
        self.fields['tags'].widget.attrs.update({'class':"input-field"})

        

class UserForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_no', 'email', 'username', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({'class':"input-field"})
        self.fields['last_name'].widget.attrs.update({'class':"input-field"})
        self.fields['phone_no'].widget.attrs.update({'class':"input-field"})
        self.fields['email'].widget.attrs.update({'class':"input-field"})
        self.fields['username'].widget.attrs.update({'class':"input-field"})
        self.fields['password1'].widget.attrs.update({'class':"input-field"})
        self.fields['password2'].widget.attrs.update({'class':"input-field"})


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_no', 'email', 'username', 'is_active', 'is_staff', 'is_superuser']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class':"input-field"})
        self.fields['last_name'].widget.attrs.update({'class':"input-field"})
        self.fields['phone_no'].widget.attrs.update({'class':"input-field"})
        self.fields['email'].widget.attrs.update({'class':"input-field"})
        self.fields['username'].widget.attrs.update({'class':"input-field"})
        self.fields['is_active'].widget.attrs.update({'class':"input"})
        self.fields['is_staff'].widget.attrs.update({'class':"input"})
        self.fields['is_superuser'].widget.attrs.update({'class':"input"})

