from django.shortcuts import render, redirect
from .models import Users, LoginManager, Secrets
from django.contrib import messages
import bcrypt

# Create your views here.

# -----> User Related Data <-----

# loads the login page
def login(request):
    return render(request, 'login.html')

# Processes the POST request made by the user to login
def loginUser(request):
    # checks to see if the login info came back with errors from the models manager
    errors = Users.objects.login_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
            return redirect('/login')
    user_list = Users.objects.filter(email = request.POST['email'])
    # if the email and password is correct then they are saved with a cookie
    if user_list:
        our_user = user_list[0]
        if bcrypt.checkpw(request.POST['password'].encode(), our_user.password.encode()):
            request.session['user_id'] = our_user.id
            return redirect('/')
        # if the email or password are inccorect then they are shown on the login page
        else:
            messages.error(request, 'Invalid info')
        return redirect('/login')

# clears the users cookies and logs them out
def logout_user(request):
    request.session.flush()
    return redirect('/login')

# loads the registration page
def createUser(request):
    return render(request, 'register.html')

# Processes data submitted by the user and adds them to the DB
def addUser(request):
    # Checks to see if user data passes validations
    errors = Users.objects.check_user(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
            return redirect('/register')
    # encrypts the password before saving it in the DB
    password = request.POST['password']
    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    # adds the user into the DB
    form = request.POST
    new_user = Users.objects.create(
        first_name = form['fname'],
        last_name = form['lname'],
        email = form['email'],
        password = hashed_pw
    )
    request.session['user_id'] = new_user.id
    return redirect('/')

# loads the page to display and edit user info
def updateUser(request):
    logged_in_user = Users.objects.get(id=request.session['user_id'])
    context = {
        'logged_in_user': logged_in_user
    }
    return render(request, 'update_user.html', context)

# updates the user info
def updateUserInfo(request):
    logged_in_user = Users.objects.get(id=request.session['user_id'])
    # Checks to see if user data passes validations
    errors = Users.objects.check_user(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, vlaue)
            return redirect('/updateUser')
    # encrypts the password before saving it in the DB
    password = request.POST['password']
    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    # updates user info in the DB
    form = request.POST
    logged_in_user.first_name = form['fname']
    logged_in_user.last_name = form['lname']
    logged_in_user.email = form['email']
    logged_in_user.password = hashed_pw
    logged_in_user.save()
    return redirect('/update')

# deletes the user and logs them out
def deleteUser(request):
    logged_in_user = Users.objects.get(id=request.session['user_id'])
    logged_in_user.delete()
    request.session.flush()
    return redirect('/login')


# -----> Secret Related Data <-----

# loads the main page
def main(request):
    logged_in_user = Users.objects.get(id=request.session['user_id'])
    context = {
        'logged_in_user': logged_in_user
    }
    return render(request, 'main.html', context)

# loads the page to update a secret
def updateSecret(request, secret_id):
    logged_in_user = Users.objects.get(id=request.session['user_id'])
    secret = Secrets.objects.get(id=secret_id)
    context = {
        'secret': secret
    }
    return render(request, 'update_secret.html', context)

# updates the secret
def updateSecretData(request, secret_id):
    logged_in_user = Users.objects.get(id=request.session['user_id'])
    # encrypts username before saving it to the DB
    username = request.POST['username']
    hashed_un = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    # encrypts password before saving it to the DB
    password = request.POST['password']
    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    # saves the data to the DB
    form = request.POST
    this_secret = Users.objects.get(id=secret_id)
    this_secret.site = form['site']
    this_secret.username = hashed_un
    this_secret.password = hashed_pw
    this_secret.save()
    return redirect('/')

# deletes secret from DB
def deleteSecret(request, secret_id):
    logged_in_user = Users.objects.get(id=request.session['user_id'])
    this_secret = Secrets.objects.get(id=secret_id)
    this_secret.delete()
    return redirect('/')

# loads the page to create a secret
def createSecret(request):
    logged_in_user = Users.objects.get(id=request.session['user_id'])
    return render(request, 'create_secret.html')

# Takes the POST data and creates a secret
def createSecretData(request):
    logged_in_user = Users.objects.get(id=request.session['user_id'])
    # encrypts the password before saving it in the DB
    username = request.POST['username']
    hashed_un = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    # encrypts the password before saving it in the DB
    password = request.POST['password']
    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    # adds the secret into the DB
    form = request.POST
    new_user = Users.objects.create(
        site = form['site'],
        username = form['username'],
        password = form['password'],
    )
    return redirect('/')

# loads the page to view secret info
def viewSecret(request, secret_id):
    logged_in_user = Users.objects.get(id=request.session['user_id'])
    secret = Secrets.objects.get(id=secret_id)
    context = {
        'secret': secret
    }
    return render(request, 'view_secret.html', context)