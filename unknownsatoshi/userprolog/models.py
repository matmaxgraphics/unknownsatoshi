import uuid
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import Group
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin



class UserManager(BaseUserManager):

    def create_superuser(self, email, username, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("superuser should be set to is_staff=True")
        
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("superuser should be set to is_superuser=True")

        return self.create_user(email, username, password, **extra_fields)

    def create_user(self, email, username, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("superuser should be set to is_staff=True")

        if not email:
            raise ValueError("Email is required")
        
        if not username:
            raise ValueError("Username is required")

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    username = models.CharField(max_length=200, unique=True, blank=True)
    email = models.EmailField(max_length=200, unique=True, blank=False)
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    phone_no = models.CharField(max_length=11, blank=True,)
    profile_picture = models.ImageField(upload_to="images/profile_image",default="default_user_image.jpeg", blank=True, null=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = UserManager()
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email',]

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("admin-update-user", kwargs={"pk": self.pk})
    


@receiver(post_save, sender=User)
def create_profile(sender, instance, **kwargs):
    user = instance
    if  user.is_staff == False and user.is_active == True and user.is_superuser == True:
        group = Group.objects.get(id=1)
        instance.groups.add(group)
        print("user profile has been created")

    #     # adds general users to user group
    # elif user.is_active == True and user.is_staff == False and user.is_superuser == False:
    #     group = Group.objects.get_or_create(name="user")
    #     if Group.objects.filter(name=group.name).exists():
    #         instance.groups.add(group)
    #         print("user profile has been created")