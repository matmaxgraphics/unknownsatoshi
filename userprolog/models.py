import uuid
from django.db import models
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.validators import MaxLengthValidator
from django.contrib.auth.models import Group, Permission
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
    phone_no = models.CharField(max_length=11,validators=[MaxLengthValidator(11)])
    profile_picture = models.ImageField(null=True, blank=True, default="default_user_image.jpeg", upload_to="profile_image/",)
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
def create_profile(sender, created, instance, **kwargs):
    user = instance
    if created and user.is_superuser:
        admin_group, created = Group.objects.get_or_create(name='admin')
        permission_list = Permission.objects.all()
        admin_group.permissions.set(permission_list)
        admin_group.user_set.add(user)
        admin_group.save()
        return admin_group

    elif user.is_superuser == False and user.is_staff == False:
        user_group, created = Group.objects.get_or_create(name='user')
        user_group.user_set.add(user)
        user_group.save()
        return user_group
    