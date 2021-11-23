from django.forms import ModelForm, fields
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Cms, Course, Store, Blog

class CmsForm(ModelForm):
    class Meta:
        model = Cms
        fields = ['title', 'entry', 'stoploss', 'tp_target', 'tp_achieved', 'profit',]
    
    def __init__(self, *args, **kwargs):
        super(CmsForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

        # self.fields['title'].widget.attrs.update(
        #     {'class': 'input'})

        # self.fields['description'].widget.attrs.update(
        #     {'class': 'input'})
class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['poststitle', 'postsauthour', 'posts', 'featured_image','featured_stories','latest_news','latest_articles']
    
    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)

        self.fields['poststitle'].widget.attrs.update(
            {'class': 'input'})
        
        self.fields['postsauthour'].widget.attrs.update(
            {'class': 'input'})
        
        self.fields['posts'].widget.attrs.update(
            {'class': 'input'})

        self.fields['featured_stories'].widget.attrs.update(
            {'class': 'input'})

        self.fields['latest_news'].widget.attrs.update(
            {'class': 'input'})

        self.fields['latest_articles'].widget.attrs.update(
            {'class': 'input'})



class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['courses', 'course_link', 'featured_image', ]
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
    
    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

class StoreForm(ModelForm):
    class Meta:
        model = Store
        fields = ['stores', 'stores_link','price', 'featured_image', 'tags']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
    
    def __init__(self, *args, **kwargs):
        super(StoreForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


