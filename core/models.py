import uuid as uuid
from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.ForeignKey(User, related_name="user_profile", on_delete=models.CASCADE)
    account_number = models.CharField(max_length=255, blank=True, null=True)
    shaba_number = models.CharField(max_length=255, blank=True, null=True)

    name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    father_name = models.CharField(max_length=255, blank=True, null=True)
    meli_number = models.CharField(max_length=255, blank=True, null=True)
    sh_number = models.CharField(max_length=255, blank=True, null=True)

    mobile_number = models.CharField(max_length=255, blank=True, null=True)
    
    land_number = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=255, blank=True, null=True)
    city = models.ForeignKey(City, related_name="user_profile", on_delete=models.CASCADE, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)

class Gate(models.Model):
    profile = models.ForeignKey(UserProfile, related_name="gates", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    url = models.CharField(max_length=255)

    gate_token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return str(self.title)

class Product(models.Model):
    profile = models.ForeignKey(UserProfile, related_name="products", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)

    def __str__(self):
        return str(self.title)



