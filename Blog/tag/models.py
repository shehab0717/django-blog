from django.db import models

class Tag(models.Model):
    name=models.CharField(max_length=20, primary_key=True)

    def __str__(self) -> str:
        return self.name