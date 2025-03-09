from django.db import models
from enum import Enum
# Create your models here.


class Item(models.Model):
    '''Item Model with Predefined Category & Subcategory'''
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='items/images/', blank=True, null=True)
    manufacturer = models.CharField(max_length=100)
    count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=100)

    class Category(Enum):
        ELECTRONICS = 'Electronics'
        FASHION = 'Fashion'
        HOME = 'Home'
        SPORTS = 'Sports'
        OTHER = 'Other'

        def coices(self):
            return [(tag.name, tag.value) for tag in self]
    
    category = models.CharField(max_length=20, choices=Category.coices(), default=Category.OTHER)

    def __str__(self):
        return self.name

