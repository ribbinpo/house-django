from distutils.command.upload import upload
from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class tb_house(models.Model):
    name_house = models.CharField(max_length=255)
    address_house = models.TextField()
    detail_house = models.TextField()
    photo_house = models.ImageField(upload_to="photo",default='')
    price_house = models.IntegerField()
    status_house = models.BooleanField()
    date_house = models.DateTimeField(auto_now=True, blank=False)

class tb_user(models.Model):
    firstname_user = models.CharField(max_length=255)
    lastname_user = models.CharField(max_length=255)
    age_user = models.IntegerField()
    email_user = models.CharField(max_length=255)
    phone_user = models.CharField(max_length=100)
    sex_user = models.CharField(max_length=200)