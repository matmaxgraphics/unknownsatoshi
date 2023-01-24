from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm




@admin.register(User)
class AdminUser(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('username', 'email', 'first_name', 'last_name', 'phone_no', 'is_active', 'is_staff', 'is_superuser')
    readonly_fields = ("id", "created", "updated", "date_joined")
    ordering = ('email',)
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "id",
                    "first_name",
                    "last_name",
                    "phone_no",
                    "email",
                    "username",
                    "password1",
                    "password2",
                    "profile_picture",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "user_permissions",
                    "created",
                    "updated"
                ),
            },
        ),
    )
    fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "id",
                    "first_name",
                    "last_name",
                    "phone_no",
                    "email",
                    "username",
                    "password",
                    "profile_picture",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "user_permissions",
                    "created",
                    "updated"
                ),
            },
        ),
    )