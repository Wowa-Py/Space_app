from django.db import models
from datetime import date

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    birthdate = models.DateField(default=date.today)

    def __str__(self):
        return self.name


