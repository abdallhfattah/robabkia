from django.db import models

# Create your models here.


class Transaction(models.Model):
    """Transaction Model with Predefined Status"""

    buyer = models.ForeignKey(
        "user.Account", on_delete=models.CASCADE, related_name="purchases"
    )
    seller = models.ForeignKey(
        "user.Account", on_delete=models.CASCADE, related_name="sales"
    )
    offer = models.ForeignKey("offer.Offer", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item.name


class Feedback(models.Model):
    """Feedback Model with Predefined Rating"""

    offer = models.ForeignKey("offer.Offer", on_delete=models.CASCADE)
    rater = models.ForeignKey("user.Account", on_delete=models.CASCADE)
    # TODO: NEEDS FIXING
    # rating = models.enumeratedField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        message = f"sold offer for {self.offer.sold_price} : Transaction between {self.buyer} and {self.seller}"
        return message
