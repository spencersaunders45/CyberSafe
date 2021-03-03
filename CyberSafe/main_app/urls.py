from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login),
    path('login/process', views.loginUser),
    path('logout', views.logout_user),
    path('register', views.createUser),
    path('register/process', views.addUser),
    path('', views.main),
    path('update/<int:secret_id>', views.updateSecret),
    path('delete/<int:secret_id>', views.deleteSecret),
    path('create', views.createSecret),
    path('create/process', views.createSecretData),
    path('view/<int:secret_id>', views.viewSecret),
    path('update', views.updateUser),
    path('delete', views.deleteUser)
]