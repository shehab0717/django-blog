from django.db import models

class BadWord(models.Model):
    text = models.TextField(max_length=100)