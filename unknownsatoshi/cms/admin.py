from django.contrib import admin

# Register your models here.
from .models import Cms, Product, Subscription, Tag, Review, Course, Product, Blog

# admin.site.register(Cms)
# admin.site.register(Tag)
# admin.site.register(Review)
# admin.site.register(Course)
# admin.site.register(Store)
# admin.site.register(Blog)



@admin.register(Cms)
class AdminCms(admin.ModelAdmin):
    list_display = ('title','entry','stoploss','tp_target','tp_achieved','profit','featured_image','created')


@admin.register(Tag)
class AdminTag(admin.ModelAdmin):
    list_display = ('name', 'created')


@admin.register(Review)
class AdminReview(admin.ModelAdmin):
    list_display = ('trade', 'body', 'value', 'created')


@admin.register(Course)
class AdminCourse(admin.ModelAdmin):
    list_display = ('courses', 'course_link', 'featured_image')


@admin.register(Product)
class AdminStore(admin.ModelAdmin):
    list_display = ('product_name', 'product_link', 'price', 'featured_image')


@admin.register(Blog)
class AdminBlog(admin.ModelAdmin):
    list_display = ('title','author','post','featured_stories','latest_news','latest_articles','featured_image', 'premium')
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Subscription)
class AdminSubscription(admin.ModelAdmin):
    list_display = ('title', 'price', 'start_date', 'expiry_date')
    prepopulated_fields = {"slug": ("title",)}