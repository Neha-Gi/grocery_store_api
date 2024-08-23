from django.db import models

# Create your models here.

class Review(models.Model):

    RATING_CHOICES = [
        ('1', 'Very Bad'),
        ('2', 'Bad'),
        ('3', 'Average'),
        ('4', 'Good'),
        ('5', 'Excellent')
    ]
    customer=models.ForeignKey('customer.Customer',on_delete=models.CASCADE, related_name='customer', null = True)
    product=models.ForeignKey('product.Product',on_delete=models.CASCADE, related_name='product', null = True)
    rating = models.CharField(choices = RATING_CHOICES, null=True, default = '3')
    comments = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f'Product_ID: {self.product}, Customer: {self.customer}, Rating: {self.rating}'