from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.ForeignKey(User, related_name="user_profile", on_delete=models.CASCADE)
    account_number = models.CharField(max_length=255, blank=True, null=True)
    shaba_number = models.CharField(max_length=255, blank=True, null=True)

class Gate(models.Model):
    profile = models.ForeignKey(UserProfile, related_name="gates", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    url = models.CharField(max_length=255)


class Product(models.Model):
    profile = models.ForeignKey(UserProfile, related_name="products", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.IntegerField()



