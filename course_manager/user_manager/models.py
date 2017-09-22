from django.db import models
import re

# Create your models here.
class Users_valid(models.Manager):
    def user_validator(self, postData):
        errors = {}
        if not re.match(r'^\D+', postData['name']):
            errors['name'] = 'Name may not include digits.'
        if postData['password'] != postData['confirm_password']:
            errors['password'] = 'Password must match password confirmation.'
        if len(Users.objects.filter(email=postData['email'])):
            errors['email'] = 'Email must be unique.'
        return errors


class Users(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=60, unique=True)
    password = models.CharField(max_length=255)
    objects = Users_valid()
