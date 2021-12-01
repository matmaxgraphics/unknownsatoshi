from django.contrib import admin
from .models import User




@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'phone_no', 'profile_picture', 'is_active', 'is_staff', 'is_superuser')