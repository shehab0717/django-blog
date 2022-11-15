from django.shortcuts import render, redirect
from .forms import CreatePostForm

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