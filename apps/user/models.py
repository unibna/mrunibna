from django.db import models
from django.contrib.auth.models import AbstractUser

DEFAULT_AVATAR = 'avatar/default.png'

class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/', default=DEFAULT_AVATAR)

    def __str__(self):
        return self.username

