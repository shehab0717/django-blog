from django.db import models
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from category.models import Category

class Tag(models.Model):
    name=models.CharField(max_length=20, primary_key=True)

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    author_id = models.ForeignKey(User, on_delete= models.CASCADE)
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)

    def get_all(self):
        return self.objects.all()

    def get_by_category(self, category_id):
        category = get_object_or_404(Category, id = category_id)
        if category:
            return self.objects.filter(category_id = category)
        return None

class PostReaction(models.Model):
    liked = models.BooleanField()
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    text = models.TextField()
    is_reply = models.BooleanField(default=False)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    parent_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)