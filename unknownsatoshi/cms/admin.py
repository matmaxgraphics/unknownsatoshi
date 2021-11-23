from django.contrib import admin

# Register your models here.
from .models import Cms, Tag, Review, Course, Store, Adminlogin, Blog

admin.site.register(Cms)
admin.site.register(Tag)
admin.site.register(Review)
admin.site.register(Course)
admin.site.register(Store)
admin.site.register(Adminlogin)
admin.site.register(Blog)