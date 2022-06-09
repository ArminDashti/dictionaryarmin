from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('words/', views.words_list),
    path('words/<int:pk>/', views.words_list),
    path('users/', views.UserList.as_view()),
    path('usersd/', views.UserDetail.as_view()),
    path('api-auth/', include('rest_framework.urls')),

]

urlpatterns = format_suffix_patterns(urlpatterns)