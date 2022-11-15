from django.db import models
from django.contrib.auth.models import User
from category.models import Category

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    author_id = models.ForeignKey(User, on_delete= models.CASCADE)
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)


class PostReaction(models.Model):
    liked = models.BooleanField()
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Tag(models.Model):
    name=models.CharField(max_length=20, primary_key=True)
    posts = models.ManyToManyField(Post)

class Comment(models.Model):
    text = models.TextField()
    is_reply = models.BooleanField(default=False)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    parent_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)