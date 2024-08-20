from django.db import models

# Create your models here.

class Customer(models.Model):
    username = models.CharField(max_length=50, unique=True, null=False)
