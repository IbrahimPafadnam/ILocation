from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', include('pages.urls')),
    path('biens/', include('biens.urls')),
    path('comptes/', include('comptes.urls')),
    path('contacts/', include('contacts.urls')),
    path('commentaire/', include('commentaire.urls')),
    path('meeee/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

#Erreur 404
handler404 ="pages.views.handler404"