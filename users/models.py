from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="First Name")
    last_name = models.CharField(max_length=100, verbose_name="Last Name")
    email = models.CharField(max_length=200, verbose_name="Email")
    password = models.CharField(max_length=200, verbose_name="Password")
    city = models.CharField(max_length=200, verbose_name="City")
