
from django.contrib import admin
from django.urls import path,include

# For read media file
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.urls import re_path as url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("player.urls")),

    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]


urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)