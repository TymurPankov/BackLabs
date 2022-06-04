from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='pictures')
    bio = models.DateField()
    email = models.EmailField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username




