# Created Model for Telegram Users

from django.db import models

class TelegramUser(models.Model):
    username = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.username
