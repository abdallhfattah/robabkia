from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
class User(AbstractUser):
    phone = PhoneNumberField()
    bio = models.TextField(verbose_name="Bio", blank=True, null=True)
    dob = models.DateField(verbose_name="Date of Birth", blank=True, null=True)
    location = models.CharField(verbose_name="Location", max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username
