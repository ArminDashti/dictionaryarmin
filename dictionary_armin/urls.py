from django.urls import path
from . import views

app_name = 'dictionary_armin'

urlpatterns = [
    path('insword/', views.insword, name='insword'),
    path('rw/', views.randomword, name='randomword'),
]

#Ramin Dashti
