from django.db import models


# Create your models here.
class Form(models.Model):
    name = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=255, null=True)
    password = models.CharField(max_length=255, null=True)
