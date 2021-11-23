from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Cms(models.Model):
    title = models.CharField(max_length=200)
    entry = models.TextField(null=True, blank=True)
    stoploss = models.TextField(null=True, blank=True)
    tp_target = models.IntegerField(default=0, null=True, blank=True)
    tp_achieved = models.IntegerField(default=0, null=True, blank=True)
    profit = models.IntegerField(default=0, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    featured_image = models.ImageField(null=True, blank=True, default="default.jpg")
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title

class Review(models.Model):
    TRADE_TYPE = (
        {'Buy', 'BUY'},
        {'Sell', 'SELL'},
    )
    #owner = 
    trade = models.ForeignKey(Cms, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=TRADE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.value


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name

class Course(models.Model):
    courses = models.TextField(null=True, blank=True)
    course_link = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(null=True, blank=True, default="default.png")
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.courses

class Store(models.Model):
    stores = models.TextField(null=True, blank=True)
    stores_link = models.TextField(null=True, blank=True)
    price = models.TextField(null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    featured_image = models.ImageField(null=True, blank=True, default="default.png")
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.stores

class Adminlogin(models.Model):
    name  = models.TextField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Blog(models.Model):
    poststitle = models.TextField(null=True, blank=True)
    postsauthour = models.CharField(max_length=200, null=True)
    posts = models.TextField(max_length=200, null=True, blank=True)
    featured_stories = models.BooleanField(default=False)
    latest_news = models.BooleanField(default=False)
    latest_articles = models.BooleanField(default=False)
    featured_image = models.ImageField(null=True, blank=True, default="default.png")
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.poststitle