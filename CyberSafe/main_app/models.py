from django.db import models
from .crypter import PasswordChecker

# Create your models here.
class LoginManager(models.Manager):
  def check_user(self, postData):
    errors = {}
    if len(postData['fname']) < 3:
      errors['fname'] = "First name needs 3 or more characters"
    if len(postData['lname']) < 3:
      errors['lname'] = "Last name needs 3 or more characters"
    if len(postData['password']) != 20:
      errors['password'] = 'Password must be 20 characters'
    if (postData['password'] != postData['confirm_pw']):
      errors['password'] = 'Passwords do not match'
    if PasswordChecker.numberCheck(postData['password']):
      errors['password'] = PasswordChecker.numberCheck(postData['password'])
    if PasswordChecker.capLettersCheck(postData['password']):
      errors['password'] = PasswordChecker.capLettersCheck(postData['password'])
    if PasswordChecker.lowerLettersCheck(postData['password']):
      errors['password'] = PasswordChecker.lowerLettersCheck(postData['password'])
    if PasswordChecker.symbolCheck(postData['password']):
      errors['password'] = PasswordChecker.symbolCheck(postData['password'])
    return errors
  def login_validator(self, post_data):
    errors = {}
    if len(post_data['email']) < 7:
      errors['email'] = 'Email too short'
    if len(post_data['password']) < 7:
      errors['password'] = 'Password too short'
    return errors

class Users(models.Model):
  first_name = models.CharField(max_length=15)
  last_name = models.CharField(max_length=15)
  email = models.CharField(max_length=40)
  password = models.CharField(max_length=40)
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)
  objects = LoginManager()

class Secrets(models.Model):
  user = models.ForeignKey(Users, related_name='secret_info', on_delete = models.CASCADE)
  site = models.CharField(max_length=15)
  username = models.CharField(max_length=15)
  password = models.CharField(max_length=40)
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)