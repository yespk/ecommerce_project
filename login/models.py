from django.db import models


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=60)
    mobile = models.CharField(max_length=12)
    password = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
