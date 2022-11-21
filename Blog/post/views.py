from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import CreatePostForm, CreateCommentForm
from .models import Post, PostReaction, Comment, Reply
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
        comment.post_id = post
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
    user_reaction = post.user_reaction(request.user)
    reaction_number = 0
    if user_reaction:
        user_reaction = user_reaction.first()
        if user_reaction.liked:
            reaction_number = 1
        else:
            reaction_number = -1
    context['user_reaction'] = reaction_number
    if request.POST:
        if 'reaction' in request.POST:
            _react(request, post)
        elif 'reply_text' in request.POST:
            _send_reply(request)
        else:
            commentForm = _create_comment(request, post)
            context['commentForm'] = commentForm
        return redirect(reverse('post_details', args = [id]))
    return render(request, 'post/details.html', context)


@login_required
def post_update(request, id):
    post = Post.objects.get(pk=id)
    if request.user == post.author_id or (request.user and request.user.is_staff):
        if request.POST:
            form = CreatePostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                form.save()
                next = request.GET.get('next')
                if not next:
                    next = reverse('post_details', kwargs={'id': id})
                return redirect(next)
            return render(request, 'post/update.html', {'form': form})
        form = CreatePostForm(instance=post)

        return render(request, 'post/update.html', {'form': form})
    raise PermissionDenied()


@login_required
def post_delete(request, id):
    post = Post.objects.filter(id=id)
    if not post:
        return render(request, 'shared/not_found.html')
    post = post.first()
    if request.POST:
        if not request.user == post.author_id:
            raise PermissionDenied()
        post.delete()
        return redirect(reverse('home'))
    return render(request, 'post/delete.html', {'post': post})


def _send_reply(request):
    if request.POST:
        reply = Reply()
        reply.text = request.POST['reply_text']
        print(request.POST)
        comment = Comment.objects.get(pk=request.POST['comment_id'])
        reply.comment_id = comment
        reply.author_id = request.user
        reply.save()
