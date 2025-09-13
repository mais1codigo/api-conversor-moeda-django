# core/urls.py

from django.urls import path
from . import views 

urlpatterns = [
    
    path('converter/', views.CurrencyConverterView.as_view(), name='converter'),
]
