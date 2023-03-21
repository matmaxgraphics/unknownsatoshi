import uuid
import decimal
from django.db import models
from cms import plans_helper
from userprolog.models import User
from django.urls import reverse
from datetime import datetime
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.template.defaultfilters import slugify
from django.core.exceptions import ValidationError
from ckeditor_uploader.fields import RichTextUploadingField



def validate_existing_plan(value):
    if FirstTimePlan.objects.filter(title=value).exists():
        raise ValidationError(f"{value} already exist on the table")

    if Plan.objects.filter(title=value).exists():
        raise ValidationError(f"{value} already exist on the table")
    return value

today = datetime.now().date()


class ProductCategory(models.Model):
    name = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.name


class Cms(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=200)
    entry = models.CharField(max_length=200,null=True, blank=True)
    stoploss = models.CharField(max_length=200,null=True, blank=True)
    tp_target = models.CharField(max_length=200,default=0, null=True, blank=True)
    tp_achieved = models.CharField(max_length=200,default=0, null=True, blank=True)
    profit = models.CharField(max_length=200,default=0, null=True, blank=True)
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
    title = models.CharField(max_length=2000)
    slug = models.SlugField(max_length=2000, blank=False, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=True)
    post = RichTextUploadingField()
    featured_stories = models.BooleanField(default=False)
    latest_news = models.BooleanField(default=False)
    latest_articles = models.BooleanField(default=False)
    featured_image = models.ImageField(null=True, blank=True, default="default.png", upload_to="blog_images/")
    premium = models.BooleanField(default=False)
    home_page = models.BooleanField(default=False)
    
    #like model field
    likes = models.ManyToManyField(User, related_name="likes")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-created_on', 'updated_on']

    def __str__(self):
        return self.title

    def snippet(self):
        return self.post[:200]

    def meta_snippet(self):
        return self.post[:50]
    
    @property
    def commenters(self):
        queryset = self.comment_set.all()
        return queryset

    def get_absolute_url(self):
        return reverse("blog-detail", kwargs={"slug": self.slug})


#views count models
class ViewCount(models.Model):
    blog=models.ForeignKey(Blog, related_name="view_count", on_delete=models.CASCADE)
    ip_address=models.CharField(max_length=50)
    session=models.CharField(max_length=50, null= True)

    def __str__(self):
        return str(self.ip_address)


#comment model
class Comment(models.Model):
    owner= models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    blog= models.ForeignKey(Blog, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)
    
    class Meta:
        ordering = ['-created']
    
    def __str__(self):
        return str(self.blog)

#subscription plan for premium blog views 
class Plan(models.Model):
    title = models.CharField(max_length=90, choices=plans_helper.main_plans)
    slug = models.SlugField(unique=False, null=True, blank=True)
    desc = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percentage = models.IntegerField(default=0)
    duration_in_days = models.IntegerField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ("created_on",)

    def __str__(self):
        return f"{self.duration_in_days} days {self.title}"

    def discount(self):
        discount_price = decimal.Decimal(self.discount_percentage / 100) * decimal.Decimal(self.price)
        return round(discount_price, 2)

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(self.title)

        discount_price = decimal.Decimal(self.discount_percentage / 100) * decimal.Decimal(self.price)
        self.discount_price = self.price - discount_price

        if self.title == "weekly plan":
            self.duration_in_days = 7
        elif self.title == "monthly plan":
            self.duration_in_days = 30
        elif self.title == "quarterly plan":
            self.duration_in_days = 90
        elif self.title == "half a year plan":
            self.duration_in_days = 180
        elif self.title == "a year plan":
            self.duration_in_days = 365
        else:
            True
        return super().save(*args, **kwargs)


# this saves the subscriptin record
class SubscriptionHistory(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=200, unique=False, blank=False)
    full_name = models.CharField(max_length=200, blank=False)
    phone_no = models.CharField(max_length=11, unique=False, blank=False)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, default='monthly plan')
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    reference = models.CharField(max_length=200, unique=True, blank=False)
    transaction_id = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    start_date = models.DateField(default=today)
    expiry_date = models.DateField(default=None)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


@receiver(pre_save, sender=SubscriptionHistory)
def update_activeness(sender, instance, *args, **kwargs):
    if instance.expiry_date <= today:
        instance.active = False
    else:
        instance.active = True
    

class Newsletter(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.email


# First time subscription plan
class FirstTimePlan(models.Model):
    title = models.CharField(max_length=90, choices=plans_helper.first_time_plans)
    slug = models.SlugField(unique=False, null=True, blank=True)
    desc = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percentage = models.IntegerField(default=0)
    duration_in_days = models.IntegerField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ("created_on",)

    def __str__(self):
        return f"{self.duration_in_days} days {self.title}"

    def discount(self):
        discount_price = decimal.Decimal(self.discount_percentage / 100) * decimal.Decimal(self.price)
        return round(discount_price, 2)
        
    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(self.title)
        discount_price = decimal.Decimal(self.discount_percentage / 100) * decimal.Decimal(self.price)
        self.discount_price = self.price - discount_price
        
        if self.title == "weekly plan":
            self.duration_in_days = 7
        elif self.title == "monthly plan":
            self.duration_in_days = 30
        elif self.title == "quarterly plan":
            self.duration_in_days = 90
        elif self.title == "half a year plan":
            self.duration_in_days = 180
        elif self.title == "a year plan":
            self.duration_in_days = 365
        else:
            True
        return super().save(*args, **kwargs)


# This saves the subscriptin record for first time subscripbers with discount
class FirstTimeSubscriptionHistory(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=200, unique=False, blank=False)
    full_name = models.CharField(max_length=200, blank=False)
    phone_no = models.CharField(max_length=11, unique=False, blank=False)
    plan = models.ForeignKey(FirstTimePlan, on_delete=models.CASCADE, default='monthly plan')
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    reference = models.CharField(max_length=200, unique=True, blank=False)
    transaction_id = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    start_date = models.DateField(default=today)
    expiry_date = models.DateField(default=None)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


@receiver(pre_save, sender=FirstTimeSubscriptionHistory)
def update_activeness(sender, instance, *args, **kwargs):
    if instance.expiry_date <= today:
        instance.active = False
    else:
        instance.active = True