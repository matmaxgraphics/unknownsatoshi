
from userprolog.models import User
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from ckeditor_uploader.widgets import CKEditorUploadingWidget


        

class CmsForm(forms.ModelForm):
    title = forms.CharField(required=True)
    entry = forms.CharField(max_length=500, required=True)
    stoploss = forms.CharField(max_length=500, required=True)
    tp_target = forms.CharField(max_length=500, required=True)
    tp_achieved = forms.CharField(max_length=500, required=True)
    profit = forms.CharField(max_length=500, required=True)
    
    class Meta:
        model = Cms
        fields = ['title', 'entry', 'stoploss', 'tp_target', 'tp_achieved', 'profit']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({"class": "input-field", 'placeholder':"title"})
        self.fields['entry'].widget.attrs.update({'class': "input-field", 'placeholder':"entry"})
        self.fields['stoploss'].widget.attrs.update({'class': "input-field", 'placeholder':"stop loss"})
        self.fields['tp_target'].widget.attrs.update({'class': "input-field", 'placeholder':"tp target"})
        self.fields['tp_achieved'].widget.attrs.update({'class': "input-field", 'placeholder':"tp achieved"})
        self.fields['profit'].widget.attrs.update({'class': "input-field", 'placeholder':"profit"})

        
class BlogForm(forms.ModelForm):
    title = forms.CharField(required=True)
    post = forms.CharField(widget=CKEditorUploadingWidget(), required=True)
    featured_image = forms.ImageField(required=False, error_messages={'required':"An image is required"})
    
    class Meta:
        model = Blog
        fields = ['title', 'slug', 'post', 'featured_image','featured_stories','latest_news','latest_articles', 'premium', 'home_page']
        exclude = ['author']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({'class': "input-field", 'placeholder':"title"})
        self.fields['slug'].widget.attrs.update({'class': "input-field", 'placeholder':"slug title"})
        self.fields['post'].widget.attrs.update({'placeholder':"post"})
        self.fields['featured_image'].widget.attrs.update({'class': "input-field", 'placeholder':"image"})
        self.fields['featured_stories'].widget.attrs.update({})
        self.fields['latest_news'].widget.attrs.update({})
        self.fields['latest_articles'].widget.attrs.update({})
        self.fields['home_page'].widget.attrs.update({})
        self.fields['premium'].widget.attrs.update({})        


class CourseForm(forms.ModelForm):
    courses = forms.CharField(required=True)
    course_link = forms.URLField(error_messages={'required':"Website link to product"})
    featured_image = forms.ImageField(required=False, error_messages={'required':"An image is required"})
    
    class Meta:
        model = Course
        fields = ['courses', 'course_link']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['courses'].widget.attrs.update({'class':"input-field", 'placeholder':"course"})
        self.fields['course_link'].widget.attrs.update({'class':"input-field", 'placeholder':"course link"})
        self.fields['featured_image'].widget.attrs.update({'class':"input-field"})


class ProductForm(forms.ModelForm):
    featured_image = forms.ImageField(required=False, error_messages={'required':"An image is required"})

    class Meta:
        model = Product
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product_category'].widget.attrs.update({'class':"input-field"})
        self.fields['product_name'].widget.attrs.update({'class':"input-field"})
        self.fields['product_link'].widget.attrs.update({'class':"input-field"})
        self.fields['price'].widget.attrs.update({'class':"input-field"})
        self.fields['featured_image'].widget.attrs.update({'class':"input-field"})


class ProductUpdateForm(forms.ModelForm):
    featured_image = forms.ImageField(required=False, error_messages={'required':"An image is required"})
    
    class Meta:
        model = Product
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product_category'].widget.attrs.update({'class':"input-field"}, required=True)
        self.fields['product_name'].widget.attrs.update({'class':"input-field"}, required=True)
        self.fields['product_link'].widget.attrs.update({'class':"input-field"}, required=True)
        self.fields['price'].widget.attrs.update({'class':"input-field"}, required=True)
        self.fields['featured_image'].widget.attrs.update({'class':"input-field"})


# user creation form for admin and users
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


# user update form for admin
class UserUpdateForm(forms.ModelForm):
    profile_picture = forms.ImageField(required=False, error_messages={'required':"An image is required"})
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_no', 'email', 'username', 'profile_picture','is_active', 'is_staff', 'is_superuser']

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


class FirstTimePlanForm(forms.ModelForm):
    discount_price = forms.DecimalField(required=False)
    duration_in_days = forms.IntegerField(required=False)

    class Meta:
        model = FirstTimePlan
        fields = '__all__'
        excluded = ('slug',)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class':"input-field"})
        self.fields['desc'].widget.attrs.update({'class':"input-field"})
        self.fields['price'].widget.attrs.update({'class':"input-field"})
        self.fields['discount_percentage'].widget.attrs.update({'class':"input-field"})
        self.fields['discount_price'].widget.attrs.update({'class':"input-field"})
        self.fields['duration_in_days'].widget.attrs.update({'class':"input-field"})
        self.fields['discount_price'].disabled=True
        self.fields['duration_in_days'].disabled=True


class FirstTimePlanUpdateForm(forms.ModelForm):
    title = forms.CharField(max_length=70)
    discount_price = forms.DecimalField(required=False)
    duration_in_days = forms.IntegerField(required=False)
    
    class Meta:
        model = FirstTimePlan
        fields = '__all__'
        excluded = ('slug',)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class':"input-field"})
        self.fields['desc'].widget.attrs.update({'class':"input-field"})
        self.fields['price'].widget.attrs.update({'class':"input-field"})
        self.fields['discount_percentage'].widget.attrs.update({'class':"input-field"})
        self.fields['discount_price'].widget.attrs.update({'class':"input-field"})
        self.fields['duration_in_days'].widget.attrs.update({'class':"input-field"})
        self.fields['discount_price'].disabled=True
        self.fields['duration_in_days'].disabled=True


class PlanForm(forms.ModelForm):
    discount_price = forms.DecimalField(required=False)
    duration_in_days = forms.IntegerField(required=False)
    
    class Meta:
        model = Plan
        fields = '__all__'
        excluded = ('slug',)
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class':"input-field"})
        self.fields['desc'].widget.attrs.update({'class':"input-field"})
        self.fields['price'].widget.attrs.update({'class':"input-field"})
        self.fields['discount_percentage'].widget.attrs.update({'class':"input-field"})
        self.fields['discount_price'].widget.attrs.update({'class':"input-field"})
        self.fields['duration_in_days'].widget.attrs.update({'class':"input-field"})
        self.fields['discount_price'].disabled=True
        self.fields['duration_in_days'].disabled=True
    

class SubscriptionHistoryForm(forms.ModelForm):
    class Meta:
        model = SubscriptionHistory
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        self.fields['user'].widget.attrs.update({'class':"input-field"})
        self.fields['email'].widget.attrs.update({'class':"input-field"})
        self.fields['full_name'].widget.attrs.update({'class':"input-field"})
        self.fields['phone_no'].widget.attrs.update({'class':"input-field"})
        self.fields['plan'].widget.attrs.update({'class':"input-field"})
        self.fields['amount_paid'].widget.attrs.update({'class':"input-field"})
        self.fields['reference'].widget.attrs.update({'class':"input-field"})
        self.fields['transaction_id'].widget.attrs.update({'class':"input-field"})
        self.fields['status'].widget.attrs.update({'class':"input-field"})
        self.fields['active'].widget.attrs.update({'class':"input-field"})
        
        
#comment form
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

        labels = {
            'body': 'Add a comment'
        }

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})