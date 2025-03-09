from django.db import models
from enum import Enum


class Offer(models.Model):
    class OfferStatus(Enum):
        PENDING = "PENDING"
        ACCEPTED = "ACCEPTED"
        REJECTED = "REJECTED"
        SOLD = "SOLD"

    post = models.ForeignKey(
        "post.Post", on_delete=models.CASCADE, related_name="offers"
    )
    title = models.CharField(max_length=150)
    lower_bound = models.DecimalField(max_digits=10, decimal_places=2)
    upper_bound = models.DecimalField(max_digits=10, decimal_places=2)
    sold_price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )

    status = models.CharField(
        max_length=10,
        choices=[
            (status.value, status.name) for status in OfferStatus
        ],
        default=OfferStatus.PENDING.value,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.status}"
