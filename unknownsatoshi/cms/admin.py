from django.contrib import admin
from .models import *




@admin.register(ProductCategory)
class AdminProductCategory(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Cms)
class AdminCms(admin.ModelAdmin):
    list_display = ('title','entry','stoploss','tp_target','tp_achieved','profit','created')


@admin.register(Course)
class AdminCourse(admin.ModelAdmin):
    list_display = ('courses', 'course_link', 'featured_image')


@admin.register(Product)
class AdminStore(admin.ModelAdmin):
    list_display = ('product_category', 'product_name','product_link', 'price', 'featured_image')


@admin.register(Blog)
class AdminBlog(admin.ModelAdmin):
    list_display = ('author','title','slug','featured_stories','latest_news','latest_articles', 'home_page', 'premium')
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Plan)
class AdminPlan(admin.ModelAdmin):
    list_display = ('title', 'desc', 'price', 'discount_percentage', 'discount_price', 'duration_in_days', 'created_on')
    readonly_fields = ('slug', 'duration_in_days', 'discount_price')


@admin.register(SubscriptionHistory)
class AdminSubscriptionHistory(admin.ModelAdmin):
    list_display = ('email', 'user', 'full_name', 'phone_no', 'plan', 'amount_paid', 'reference', 'transaction_id', 'status', 'start_date', 'expiry_date', 'active')
    readonly_fields = ('plan','amount_paid', 'reference', 'transaction_id', 'status')


@admin.register(FirstTimePlan)
class AdminPlan(admin.ModelAdmin):
    list_display = ('title', 'slug', 'desc', 'price', 'discount_percentage', 'discount_price', 'duration_in_days', 'created_on')
    readonly_fields = ('slug', 'discount_price','duration_in_days')


@admin.register(FirstTimeSubscriptionHistory)
class AdminSubscriptionHistory(admin.ModelAdmin):
    list_display = ('email', 'user', 'full_name', 'phone_no', 'plan', 'amount_paid', 'reference', 'transaction_id', 'status', 'start_date', 'expiry_date', 'active')
    readonly_fields = ('plan','amount_paid', 'reference', 'transaction_id', 'status')

@admin.register(Newsletter)
class AdminNesletter(admin.ModelAdmin):
    list_display = ('email',)

admin.site.register(Comment)

admin.site.register(ViewCount)