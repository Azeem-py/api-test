from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    phoneNumber = models.IntegerField(unique=True)
    country = models.CharField(max_length=83, )
    bank = models.CharField(max_length=83, )
    accountName = models.CharField(max_length=100, )
    accountNumber = models.IntegerField()    
    