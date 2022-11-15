from django.shortcuts import render, redirect
from .forms import CreatePostForm, CreateCommentForm
from .models import Post

def post_create(request):
    if request.POST:
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author_id = request.user
            post.save()
            return redirect('/')
        return render(request, 'post/create.html', {'form': form})
    form = CreatePostForm()
    return render(request, 'post/create.html', {'form': form})

def _create_comment(request, post):
    commentForm = CreateCommentForm(request.POST)
    if commentForm.is_valid() and request.user:
        comment = commentForm.save(commit=False)
        comment.author_id = request.user
        comment.parent_id = post
        comment.save()
        commentForm = CreateCommentForm()
    return commentForm

def post_details(request, id):
    post = Post.objects.get(pk=id)
    comments = post.comment_set.all()
    commentForm = CreateCommentForm()
    if request.POST:
        commentForm = _create_comment(request, post)
    return render(request, 'post/details.html', {'post': post,
     'comments': comments,
     'commentForm': commentForm})
