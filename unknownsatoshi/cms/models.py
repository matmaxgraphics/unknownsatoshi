from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from userprolog.models import User
import uuid
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.widgets import CKEditorUploadingWidget



# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name

class Cms(models.Model):
    title = models.CharField(max_length=200)
    entry = models.TextField(null=True, blank=True)
    stoploss = models.TextField(null=True, blank=True)
    tp_target = models.IntegerField(default=0, null=True, blank=True)
    tp_achieved = models.IntegerField(default=0, null=True, blank=True)
    profit = models.IntegerField(default=0, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    featured_image = models.ImageField(null=True, blank=True, default="default.jpg")
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.title

class Review(models.Model):
    TRADE_TYPE = (
        ("Buy", "Buy"),
        ("Sell", "Sell"),
    )
    #owner = 
    trade = models.ForeignKey(Cms, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=TRADE_TYPE, default="Buy")
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.value

class Course(models.Model):
    courses = models.TextField(null=True, blank=True)
    course_link = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(null=True, blank=True, default="default.png")
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.courses
        

class Product(models.Model):
    product_name = models.TextField(null=True, blank=True)
    product_link = models.TextField(null=True, blank=True)
    price = models.TextField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    featured_image = models.ImageField(null=True, blank=True, default="default.png")
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.product_name

class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=False, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=True)
    post = RichTextUploadingField()
    featured_stories = models.BooleanField(default=False)
    latest_news = models.BooleanField(default=False)
    latest_articles = models.BooleanField(default=False)
    featured_image = models.ImageField(null=True, blank=True, default="default.png")
    premium = models.BooleanField(default=False)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    

    def __str__(self):
        return self.title

    def snippet(self):
        return self.post[:150]

    def get_absolute_url(self):
        return reverse("blog-detail", kwargs={"pk": self.pk})
    

class Plan(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    price = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("created_on",)

    def __str__(self):
        return self.title


class SubscriptionHistory(models.Model):
    email = models.EmailField(max_length=200, unique=True, blank=False)
    username = models.CharField(max_length=100, unique=True, blank=False)
    full_name = models.CharField(max_length=200, blank=False)
    phone_no = models.CharField(max_length=11, unique=True, blank=False)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, default='monthly plan')
    reference = models.CharField(max_length=200, unique=True, blank=False)
    start_date = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.plan


