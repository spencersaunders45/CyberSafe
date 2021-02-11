from django.shortcuts import render
import bcrypt

# Create your views here.

# -----> User Related Data <-----
def login(request):
    return render(request, 'login.html')


def createUser(request):
    return render(request, 'register.html')


def updateUser(request):
    return render(request, 'update_user.html')


def deleteUser(request):
    return render(request)


# -----> Secret Related Data <-----
def main(request):
    return render(request, 'main.html')


def updateSecret(request):
    return render(request, 'update_secret.html')


def deleteSecret(request):
    return render(request)


def createSecret(request):
    return render(request, 'create_secret.html')


def viewSecret(request):
    return render(request, 'view_secret.html')