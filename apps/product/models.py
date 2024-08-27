from django.db import models

class Product(models.Model):

    # UNIT_CHOICES = [
    #     {"kg": "Kilogram"},
    #     {"g": "Gram"},
    # ]

    CATEGORY_CHOICES = [
        ('fruits','Fruits'),
        ('vegetables','Vegetables'),
    ]

    BRAND_CHOICES =[ ("Pink Lady", "Pink Lady"), ("chiquita", "Chiquita"), ("Gala", "Gala"),("Fyffes", "Fyffes")]
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    brand = models.CharField(max_length=50, choices=BRAND_CHOICES)
    image = models.ImageField(upload_to="images/")
    price = models.DecimalField(max_digits=4, decimal_places=2)
    stock = models.IntegerField()
    # unit = models.CharField(max_length=3, choices=UNIT_CHOICES, default="kg")

    def __str__(self):
        return self.name  # wthout{}, otherwise it returns a set 

