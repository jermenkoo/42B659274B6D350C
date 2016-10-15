from django.db import models

# Create your models here.


class Query(models.Model):
    transcript = models.TextField(max_length=100000)
    encrypted_phone = models.TextField(max_length=200, primary_key=True)
    approved = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=100, blank=True)
