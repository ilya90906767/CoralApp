from django.db import models 

class User(models.Model):
    full_n = models.CharField(max_length=80)
    email = models.CharField(max_length=80)
    password = models.CharField(max_length=80)
    city = models.CharField(max_length=80, blank=True)

