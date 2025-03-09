from django.db import models

# Create your models here.

class Transaction(models.model):
    '''Transaction Model with Predefined Status'''
    
    buyer = models.ForeignKey('users.User', on_delete=models.CASCADE)
    seller = models.ForeignKey('users.User', on_delete=models.CASCADE)
    offer = models.ForeignKey('offers.Offer', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.item.name

class Feedback(models.model):
    '''Feedback Model with Predefined Rating'''
    offer = models.ForeignKey('offers.Offer', on_delete=models.CASCADE    
    rater = models.ForeignKey('users.User', on_delete=models.CASCADE)
    rating = models.enumeratedField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.transaction.item.name
