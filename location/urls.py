from django.contrib import admin
from django.urls import path, include,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve


urlpatterns = [
    path('', include('pages.urls')),
    path('biens/', include('biens.urls')),
    path('comptes/', include('comptes.urls')),
    path('contacts/', include('contacts.urls')),
    path('commentaire/', include('commentaire.urls')),
    path('meeee/', admin.site.urls),

    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) + staticfiles_urlpatterns()

#Erreur 404
handler404 ="pages.views.handler404"