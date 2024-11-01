from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=255)
    details = models.TextField()
    url = models.URLField()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    asin = models.CharField(max_length=10, unique=True)
    sku = models.CharField(max_length=50, blank=True, null=True)
    image = models.URLField()
    brand = models.ForeignKey(Brand, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
