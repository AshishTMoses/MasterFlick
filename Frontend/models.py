from django.db import models

# Create your models here.


class SubscribeDb(models.Model):
    email = models.EmailField(max_length=20, null=True, blank=True)
    username = models.CharField(max_length=20, null=True, blank=True)
    password = models.CharField(max_length=10, null=True, blank=True)





