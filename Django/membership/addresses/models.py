from django.db import models

# Create your models here.
class Address(models.Model):
    user = models.ForeignKey('account.Account', related_name="addresses" ,on_delete=models.CASCADE)

    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)