from django.urls import path
from . import views


app_name = 'enapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('djangoapi/', views.SnippetList.as_view(), name='index'),
    path("dashboard/", views.dashboard, name="dashboard"),
]