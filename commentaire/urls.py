from django.urls import path
from .views import commentaire
from . import views

urlpatterns = [
    path('avis/', views.commentaire, name='avis'),
]