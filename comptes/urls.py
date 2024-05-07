from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
                        
urlpatterns = [
    path('connexion', views.connexion, name='connexion'),
    path('inscription', views.inscription, name='inscription'),
    path('deconnexion', views.deconnexion, name='deconnexion'),


    path('reset_password', auth_views.PasswordResetView.as_view(template_name="comptes/reset_password.html"),name='reset_password'),
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name="comptes/reset_password_sent.html"),name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="comptes/reset.html"),name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="comptes/reset_password_complete.html"),name='reset_password_complete'),

    path('dashboard', views.dashboard, name='dashboard')
]