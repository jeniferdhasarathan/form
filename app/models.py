from django.db import models

# Create your models here.
from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.first_name
