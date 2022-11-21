from django.shortcuts import render, redirect
from django.urls import reverse
from .models import BadWord

# Create your views here.

def badword_index(request):
    words = BadWord.objects.all()
    return render(request, 'badword/index.html', {'words': words})

def badword_create(request):
    if request.method == 'POST':
        badword = BadWord(text = request.POST['text'])
        badword.save()
        return redirect(reverse('badword_index'))
    return render(request, 'shared/not_found.html')

def badword_delete(request, id):
    if request.POST:
        word = BadWord.objects.get(pk = id)
        word.delete()
        return redirect(reverse('badword_index'))
    return render(request, 'shared/not_found.html')