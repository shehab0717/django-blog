from django.shortcuts import render, redirect
from .forms import CreatePostForm, CreateCommentForm
from .models import Post, PostReaction

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

def _react(request, post):
    reaction = PostReaction()
    reaction.liked = True if request.POST['reaction'] == 'like' else False
    reaction.user_id = request.user
    reaction.post_id = post
    reaction.save()

def post_details(request, id):
    context = {}
    post = Post.objects.get(pk=id)
    comments = post.comment_set.all()
    likes = PostReaction.likes_count(id)
    dislikes = PostReaction.dislikes_count(id)
    context['post'] = post
    context['comments'] = comments
    context['likes'] = likes
    context['dislikes'] = dislikes
    commentForm = CreateCommentForm()
    if request.POST:
        if request.POST['reaction']:
            _react(request, post)
            likes = PostReaction.likes_count(id)
            dislikes = PostReaction.dislikes_count(id)
        else:
            commentForm = _create_comment(request, post)
            context['commentForm'] = commentForm
    return render(request, 'post/details.html', context)
