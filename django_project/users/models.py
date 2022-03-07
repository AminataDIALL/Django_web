from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):

    is_director = models.BooleanField(default=False)
    is_producer = models.BooleanField(default=True)


    def __str__(self):
        return self.name