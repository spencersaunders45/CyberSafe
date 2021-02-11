from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login),
    path('register', views.createUser),
    path('', views.main),
    path('update/', views.updateSecret), #add id to url
    path('delete/', views.deleteSecret), #add id to url
    path('create', views.createSecret),
    path('view/', views.viewSecret), #add id to url
    path('update', views.updateUser),
    path('delete', views.deleteUser)
]