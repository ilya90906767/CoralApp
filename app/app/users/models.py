from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    first_n = models.CharField(blank=True, max_length=50)
    second_n = models.CharField(blank=True, max_length=50) 
    username = models.CharField(blank=True, max_length=50)
    
    