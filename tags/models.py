from django.db import models

from products.models import Product

class Tag(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    products = models.ManyToManyField(Product, blank=True)
   
    def __str__(self):
        return self.title
    