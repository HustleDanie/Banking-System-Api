from django.db import models

# Create your models here.


class Bank(models.Model):
    bank = models.CharField(max_length=200, null=False, blank=False)
    bank_address = models.CharField(max_length=2000, null=False, blank=False)