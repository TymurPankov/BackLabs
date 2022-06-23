from django.db import models
from django.contrib.auth.models import User


class EmailUserSend(models.Model):
    user = models.ForeignKey(User, related_name='taskUser', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.email}"

    class Meta:
        verbose_name = "Email"
        verbose_name_plural = "Emails"


