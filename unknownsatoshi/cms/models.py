import uuid
from django.db import models
from django.http import request
from userprolog.models import User
from django.shortcuts import get_object_or_404
from django.urls import reverse
from datetime import date, datetime, timedelta
from ckeditor_uploader.fields import RichTextUploadingField
from userprolog.models import User
from django.contrib import messages

class ProductCategory(models.Model):
    name = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.name


class Cms(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=200)
    entry = models.TextField(null=True, blank=True)
    stoploss = models.TextField(null=True, blank=True)
    tp_target = models.IntegerField(default=0, null=True, blank=True)
    tp_achieved = models.IntegerField(default=0, null=True, blank=True)
    profit = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.title

class Course(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    courses = models.TextField(null=True, blank=True)
    course_link = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(null=True, blank=True, default="default.png", upload_to="course_images/")

    def __str__(self):
        return self.courses
        
class Product(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    product_name = models.TextField(null=True, blank=True)
    product_link = models.TextField(null=True, blank=True)
    price = models.IntegerField(default=0)
    featured_image = models.ImageField(null=True, blank=True, default="default.png", upload_to="product_images/")
   
    def __str__(self):
        return self.product_name

class Blog(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=False, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=True)
    post = RichTextUploadingField()
    featured_stories = models.BooleanField(default=False)
    latest_news = models.BooleanField(default=False)
    latest_articles = models.BooleanField(default=False)
    featured_image = models.ImageField(null=True, blank=True, default="default.png", upload_to="blog_images/")
    premium = models.BooleanField(default=False)
    home_page = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.title

    def snippet(self):
        return self.post[:200]

    def home_snippet(self):
        return self.post[:200]

    def get_absolute_url(self):
        return reverse("blog-detail", kwargs={"pk": self.pk})
    

#subscription plan for premium blog views 
class Plan(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    desc = models.TextField()
    price = models.IntegerField(default=0)
    discount_price = models.IntegerField(default=0)
    discount= models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ("created_on",)

    def __str__(self):
        return self.title

# this saves the subscriptin record
class SubscriptionHistory(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=200, unique=True, blank=False)
    full_name = models.CharField(max_length=200, blank=False)
    phone_no = models.CharField(max_length=11, unique=True, blank=False)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, default='monthly plan')
    amount_paid = models.IntegerField(default=0)
    reference = models.CharField(max_length=200, unique=True, blank=False)
    transaction_id = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    start_date = models.DateField()
    expiry_date = models.DateField()
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    # @property
    # def plan_start_date(self):
    #     start_date = datetime.now().today()
    #     return start_date


    # @property
    # def plan_expiry_date(self, slug):
    #     start_date = datetime.now().date()
    #     plan = Plan.objects.get(slug=slug)
    #     plan_id = plan.slug

    #     if plan_id == "monthly-plan":
    #         expiry_date = start_date + timedelta(days=30)
    #         return expiry_date

    #     if plan_id == "quarterly-plan":
    #         expiry_date = start_date + timedelta(days=90)
    #         return expiry_date
        
    #     if plan_id == "half-a-year-plan":
    #         expiry_date = start_date + timedelta(days=180)
    #         return expiry_date
    #     else:
    #         pass
  
    def save(self, *args, **kwargs):
        self.start_date = datetime.now().today()
        id = self.kwargs.get('id')
        plan = get_object_or_404(Plan, id=id)
        user = get_object_or_404(User, id=id)
        plan_slug = plan.id
        

        print("PLAN ID AT THE MODEL IS", plan_slug)
        print("USER ID IN MODEL IS", user.id)
        
        existing_plan = SubscriptionHistory.objects.filter(plan_id=plan.id, active=True, user_id=user.id).exists()
        if existing_plan:
            messages.error(request, "you already have an active plan, wait for expiry date before subscribing to a new plan")
        else:
            pass

        if plan_slug == "monthly-plan":
            self.expiry_date = self.start_date + timedelta(days=30)
            return self.expiry_date

        if plan_slug == "quarterly-plan":
            self.expiry_date = self.start_date + timedelta(days=90)
            return self.expiry_date
        
        if plan_slug == "half-a-year-plan":
            self.expiry_date = self.start_date + timedelta(days=180)
            return self.expiry_date
        else:
            pass

        super(self).save(*args, **kwargs)


class Newsletter(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    email = models.EmailField(max_length=100)
