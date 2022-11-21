from django.db import models

class BadWord(models.Model):
    text = models.TextField(max_length=100)

    @classmethod
    def clean(cls, text: str):
        badwords = cls.objects.all()
        for word in badwords:
            text = text.replace(word.text, '*' * len(word.text))
        return text
        