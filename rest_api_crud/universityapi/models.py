from django.db import models

# Create your models here.

class Univeristy(models.Model):
    alpha_two_code = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    web_page = models.CharField(max_length=100)
