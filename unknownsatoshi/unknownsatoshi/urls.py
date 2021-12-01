from django import urls
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cms.urls')),
    path('', include('userprolog.urls')),

    # ckeditor
    path('ckeditor/', include('ckeditor_uploader.urls')),
<<<<<<< HEAD
    
=======
>>>>>>> af2ac028e1060851709025a10821b4a1ca1a474a
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
