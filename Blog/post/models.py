from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField()
    author_id = models.ForeignKey(User, on_delete= models.CASCADE)


class PostReaction(models.Model):
    liked = models.BooleanField()
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Tag(models.Model):
    name=models.CharField(max_length=20, primary_key=True)
    posts = models.ManyToManyField(Post)