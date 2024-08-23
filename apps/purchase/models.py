from django.db import models



class Order(models.Model):
    order_transaction = models.IntegerField()
    customer_id = models.ForeignKey('customer.Customer', on_delete=models.CASCADE)
    product_id = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    purchase_date = models.DateField()
    quantity = models.IntegerField()
    purchase_cost =  models.DecimalField(max_digits=6, decimal_places=2)
     #Integerfield?
    class Meta:
        unique_together = ('order_transaction', 'customer_id', 'product_id')

 
    def __str__(self):
        return f'Order: {self.order_transaction}, Customer: {self.customer_id}, Date: {self.purchase_date}'


class Cart(models.Model):
    customer_id=models.ForeignKey('customer.Customer',on_delete=models.CASCADE)
    product_id=models.ForeignKey('product.Product',on_delete=models.CASCADE)
    quantity=models.IntegerField()

    def get_cost_per_product(self):
        return self.product_id.price
    
    def get_total_amount(self):
        return  self.quantity * self.product_id.price