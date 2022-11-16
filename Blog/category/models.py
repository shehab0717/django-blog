from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    subscribers = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def toggle_subscribe(self, user):
        sub = self.subscribers.filter(id = user.id)
        if sub:
            self.subscribers.remove(user)
        else: 
            self.subscribers.add(user.id)



    def __str__(self) -> str:
        return self.name