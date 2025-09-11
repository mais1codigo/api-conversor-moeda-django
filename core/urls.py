# core/urls.py

from django.urls import path
from . import views # Importa as views do app (o arquivo views.py que acabamos de editar)

urlpatterns = [
    # Quando alguém acessar a URL "converter/", chame a classe CurrencyConverterView
    path('converter/', views.CurrencyConverterView.as_view(), name='converter'),
]