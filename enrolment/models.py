from django.db import models

# Create your models here.
class User(models.Model):
    userid = models.TextField()
    usernumer = models.IntegerField()