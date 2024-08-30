from django.db import models



# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    # Add other custom fields here as needed
