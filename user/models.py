from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


class Account(AbstractUser):
    phone = PhoneNumberField()
    bio = models.TextField(verbose_name="Bio", blank=True, null=True)
    image = models.ImageField(upload_to="profile_pics/", null=True, blank=True)
    dob = models.DateField(verbose_name="Date of Birth", blank=True, null=True)
    location = models.CharField(
        verbose_name="Location", max_length=255, blank=True, null=True
    )
    
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="account_users",
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="account_users",
        blank=True
    )

    def __str__(self):
        return self.username
