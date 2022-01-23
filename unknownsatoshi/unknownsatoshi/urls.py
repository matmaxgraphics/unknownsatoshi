import stat
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


admin.AdminSite.site_header = 'UNKNOWN SATOSHI'
admin.AdminSite.site_title = 'Unknown Satoshi'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cms.urls')),
    path('', include('userprolog.urls')),

    # ckeditor
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

handler404 = 'cms.views.custom_page_not_found'

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
