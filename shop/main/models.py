from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_available = models.IntegerField(default=0)
    image = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'Name: {self.name} price: {self.price}'
