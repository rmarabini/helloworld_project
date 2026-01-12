# Create your models here.
from django.db import models


class Greeting(models.Model):  # provide a different greeting to each user
    name = models.CharField(max_length=100)
    message = models.CharField(max_length=200, default="Hello")

    def __str__(self):
        return f"{self.message}, {self.name}!"