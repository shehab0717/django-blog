from django.shortcuts import render, redirect, get_object_or_404
from .decorators import staff_member_required
from post.models import Post
from django.contrib.auth.models import User
from django.urls import reverse
from main.models import UserStatus


@staff_member_required(login_url='/login')
def admin_index(request):
    return render(request, 'cadmin/index.html')


@staff_member_required(login_url='/login')
def post_index(request):
    posts = Post.objects.all()
    return render(request, 'cadmin/post/index.html', {'posts': posts})


@staff_member_required(login_url='/login')
def user_index(request):
    users = User.objects.all()
    return render(request, 'cadmin/user/index.html', {'users': users})

@staff_member_required(login_url='/login')
def make_admin(request, id):
    if request.POST:
        user = get_object_or_404(User, id=id)
        user.is_staff = True
        user.save()
        return redirect(reverse('user_index'))
    return render(request, 'shared/not_found.html')

@staff_member_required(login_url='/login')
def block_user(request, id):
    if request.POST:
        user = get_object_or_404(User, id=id)
        u_status = get_object_or_404(UserStatus, user = user)
        u_status.is_blocked = not u_status.is_blocked
        u_status.save()
        return redirect(reverse('user_index'))
    return render(request, 'shared/not_found.html')