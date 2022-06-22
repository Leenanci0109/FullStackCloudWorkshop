from django.db import models

# Create your models here.
class login(models.Model):
    idlogin = models.IntegerField()
    uname = models.CharField(max_length=45)
    password = models.CharField(max_length=45)