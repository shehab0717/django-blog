from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from post.models import Post
from django.contrib.auth.models import User
from django.urls import reverse


@staff_member_required
def admin_index(request):
    return render(request, 'cadmin/index.html')


@staff_member_required
def post_index(request):
    posts = Post.objects.all()
    return render(request, 'cadmin/post/index.html', {'posts': posts})


@staff_member_required
def user_index(request):
    users = User.objects.all()
    return render(request, 'cadmin/user/index.html', {'users': users})

@staff_member_required
def make_admin(request, id):
    if request.POST:
        user = get_object_or_404(User, id=id)
        user.is_staff = True
        user.save()
        return redirect(reverse('user_index'))
    return render(request, 'shared/not_found.html')

@staff_member_required
def block_user(request, id):
    if request.POST:
        user = get_object_or_404(User, id=id)
        user.is_active = not user.is_active
        user.save()
        return redirect(reverse('user_index'))
    return render(request, 'shared/not_found.html')