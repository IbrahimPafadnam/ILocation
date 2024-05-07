from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='biens'),
    path('<int:bien_id>', views.bien, name='bien'),
    path('recherche', views.recherche, name='recherche'),
    #path('payment/<int:bien_id>/', views.payment, name='payment'),
    #path('payment-success/<int:bien_id>/', views.PaymentSuccessful, name='payment-success'),
    #path('payment-failed/<int:bien_id>/', views.paymentFailed, name='payment-failed'),
]