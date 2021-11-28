import uuid
from django.urls import reverse
from django.db import models
from django.utils import timezone
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
    