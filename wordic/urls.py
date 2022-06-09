from django.urls import path
from . import views

app_name = 'wordic'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_page, name='login_page'),
    path('dict_table/', views.dict_table, name='dict_table'),
    path('cost/', views.cost, name='cost'),
    path('tt/', views.test_temp, name='tt'),
]