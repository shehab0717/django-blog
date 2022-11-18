from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import CreatePostForm, CreateCommentForm
from .models import Post, PostReaction
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required


@login_required
def post_create(request):
    if request.POST:
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author_id = request.user
            post.save()
            form.save_m2m()
            print(post.tags.all())
            return redirect(reverse('home'))
        return render(request, 'post/create.html', {'form': form})
    form = CreatePostForm()
    return render(request, 'post/create.html', {'form': form})

@login_required
def _create_comment(request, post):
    commentForm = CreateCommentForm(request.POST)
    if commentForm.is_valid() and request.user:
        comment = commentForm.save(commit=False)
        comment.author_id = request.user
        comment.parent_id = post
        comment.save()
        commentForm = CreateCommentForm()
    return commentForm

@login_required
def _react(request, post: Post):
    if request.user:
        reaction = post.user_reaction(request.user)
        if reaction:
            reaction.delete()
        else:
            reaction = PostReaction()
            reaction.liked = True if request.POST['reaction'] == 'like' else False
            reaction.user_id = request.user
            reaction.post_id = post
            reaction.save()


def post_details(request, id):
    post = Post.objects.get(pk=id)
    context = post.get_details()
    commentForm = CreateCommentForm()
    context['commentForm'] = commentForm
    if request.POST:
        if 'reaction' in request.POST:
            _react(request, post)
        else:
            commentForm = _create_comment(request, post)
            context['commentForm'] = commentForm
    return render(request, 'post/details.html', context)

@login_required
def post_update(request, id):
    post = Post.objects.get(pk=id)
    if request.POST:
        if not request.user == post.author_id:
            raise PermissionDenied()
        form = CreatePostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect(f"/post/details/{id}")
        return render(request, 'post/update.html', {'form': form})
    form = CreatePostForm(instance=post)

    return render(request, 'post/update.html', {'form': form})

@login_required
def post_delete(request, id):
    post = Post.objects.filter(id = id)
    if not post:
        return render(request, 'shared/not_found.html')
    post = post.first()
    if request.POST:
        if not request.user == post.author_id:
            raise PermissionDenied()
        post.delete()
        return redirect(reverse('home'))
    return render(request, 'post/delete.html', {'post': post})