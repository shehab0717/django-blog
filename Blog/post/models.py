from django.db import models
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from category.models import Category
from tag.models import Tag
from badword.models import BadWord



class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to= 'images/', null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    author_id = models.ForeignKey(User, on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @classmethod
    def get_all(cls, user):
        if user.is_authenticated:
            return Post.objects.filter(category_id__in = user.category_set.all())
        return Post.objects.all()
    @classmethod
    def get_by_category(cls, category_id):
        category = get_object_or_404(Category, id = category_id)
        if category:
            return Post.objects.filter(category_id = category)
        return None

    def get_details(self):
        context = {
            'post': self,
            'comments': self.comment_set.all(),
            'likes': PostReaction.likes(self.id),
            'dislikes': PostReaction.dislikes(self.id),
            }
        return context

    def clean_title(self):
        return BadWord.clean(self.title)

    def clean_conent(self):
        return BadWord.clean(self.content)

    def user_reaction(self, user):
        return PostReaction.objects.filter(post_id = self, user_id = user)



class PostReaction(models.Model):
    liked = models.BooleanField()
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    @classmethod
    def likes(cls, post_id):
        return cls.objects.filter(post_id=post_id, liked = True)
    @classmethod
    def dislikes(cls, post_id):
        return cls.objects.filter(post_id=post_id, liked = False)


class Comment(models.Model):
    text = models.TextField()
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def clean_text(self):
        return BadWord.clean(self.text)


class Reply(models.Model):
    text = models.TextField()
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean_text(self):
        return BadWord.clean(self.text)
