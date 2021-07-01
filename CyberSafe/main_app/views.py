from django.shortcuts import render, redirect
from .models import Users, LoginManager, Secrets
from django.contrib import messages
import bcrypt
from .crypter import Wizard, Password

# Create your views here.

# -----> User Related Data <-----

# loads the login page
def login(request):
    return render(request, 'login.html')

# Logs in the user
def loginUser(request):
    # checks for errors
    errors = Users.objects.login_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
            return redirect('/login')
    user_list = Users.objects.filter(email = request.POST['email'])
    # saves user to session
    if user_list:
        our_user = user_list[0]
        if bcrypt.checkpw(request.POST['password'].encode(), our_user.password.encode()):
            request.session['user_id'] = our_user.id
            request.session['mPassword'] = request.POST['password']
            return redirect('/')
        # notifies user of errors
        else:
            messages.error(request, 'Invalid info')
        return redirect('/login')

# clears session
def logout_user(request):
    request.session.flush()
    return redirect('/login')

# loads the registration page
def createUser(request):
    return render(request, 'register.html')

# Creates new user
def addUser(request):
    # Checks for errors
    errors = Users.objects.check_user(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
            return redirect('/register')
    # hashes the password
    password = request.POST['password']
    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    # adds the user to DB
    form = request.POST
    new_user = Users.objects.create(
        first_name = form['fname'],
        last_name = form['lname'],
        email = form['email'],
        password = hashed_pw
    )
    # saves user to session
    request.session['user_id'] = new_user.id
    request.session['mPassword'] = request.POST['password']
    return redirect('/')

# sends update_user.html
def updateUser(request):
    if 'user_id' not in request.session:
        return redirect('/login')
    else:
        logged_in_user = Users.objects.get(id=request.session['user_id'])
        context = {
            'logged_in_user': logged_in_user
        }
        return render(request, 'update_user.html', context)

# updates the user info
def updateUserInfo(request):
    if 'user_id' not in request.session:
        return redirect('/login')
    else:
        logged_in_user = Users.objects.get(id=request.session['user_id'])
        # Checks for errors
        errors = Users.objects.check_user(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
                return redirect('/updateUser')
        # hashes password
        password = request.POST['password']
        hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        # updates user info
        form = request.POST
        logged_in_user.first_name = form['fname']
        logged_in_user.last_name = form['lname']
        logged_in_user.email = form['email']
        logged_in_user.password = hashed_pw
        logged_in_user.save()
        request.session['mPassword'] = request.POST['password']
        return redirect('/')

# deletes the user and logs them out
def deleteUser(request):
    if 'user_id' not in request.session:
        return redirect('/login')
    else:
        logged_in_user = Users.objects.get(id=request.session['user_id'])
        logged_in_user.delete()
        request.session.flush()
        return redirect('/login')


# --------------------------> Secret Related Data <--------------------------------

# sends main.html
def main(request):
    if 'user_id' not in request.session:
        return redirect('/login')
    else:
        logged_in_user = Users.objects.get(id=request.session['user_id'])
        context = {
            'logged_in_user': logged_in_user,
            'secrets': Secrets.objects.filter(user_id=request.session['user_id'])
        }
        return render(request, 'main.html', context)

# sends update_secret.html
def updateSecret(request, secret_id):
    if 'user_id' not in request.session:
        return redirect('/login')
    else:
        logged_in_user = Users.objects.get(id=request.session['user_id'])
        secret = Secrets.objects.get(id=secret_id)
        password = Wizard.reappear(request.session['mPassword'], secret.password)
        context = {
            'site': secret.site,
            'username': secret.username,
            'password': password,
            'secretId': secret.id
        }
        return render(request, 'update_secret.html', context)

# updates the secret
def updateSecretData(request, secret_id):
    if 'user_id' not in request.session:
        return redirect('/login')
    else:
        logged_in_user = Users.objects.get(id=request.session['user_id'])
        secret_info = Secrets.objects.get(id=secret_id)
        # encrypts password
        password = Wizard.disappear(request.session['mPassword'],request.POST['password'])
        # saves changes
        secret_info.site = request.POST['site']
        secret_info.username = request.POST['username']
        secret_info.password = password
        secret_info.save()
        return redirect('/')

# deletes secret from DB
def deleteSecret(request, secret_id):
    if 'user_id' not in request.session:
        return redirect('/login')
    else:
        logged_in_user = Users.objects.get(id=request.session['user_id'])
        this_secret = Secrets.objects.get(id=secret_id)
        this_secret.delete()
        return redirect('/')

# sends create_secret.html
def createSecret(request):
    if 'user_id' not in request.session:
        return redirect('/login')
    else:
        logged_in_user = Users.objects.get(id=request.session['user_id'])
        context = {
            'logged_in_user': logged_in_user
        }
        return render(request, 'create_secret.html', context)

# Creates a secret
def createSecretData(request):
    if 'user_id' not in request.session:
        return redirect('/login')
    else:
        logged_in_user = Users.objects.get(id=request.session['user_id'])
        # hashes password
        password = Password.create(int(request.POST['maxLength']))
        encryptPassword = Wizard.disappear(request.session['mPassword'], password)
        # Adds secret to DB
        form = request.POST
        new_user = Secrets.objects.create(
            user = logged_in_user,
            site = form['site'],
            username = request.POST['username'],
            password = encryptPassword
        )
        return redirect('/')

# Sends view_secret.html
def viewSecret(request, secret_id):
    if 'user_id' not in request.session:
        return redirect('/login')
    else:
        logged_in_user = Users.objects.get(id=request.session['user_id'])
        secret = Secrets.objects.get(id=secret_id)
        password = Wizard.reappear(request.session['mPassword'], secret.password)
        context = {
            'siteName': secret.site,
            'password': password,
            'username': secret.username,
            'secret_id': secret.id
        }
        return render(request, 'view_secret.html', context)