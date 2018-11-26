from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    par_amount = models.PositiveIntegerField()
    order_amount = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10000, decimal_places=2)
    def __str__(self):
        return self.product_name
