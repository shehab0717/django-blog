from django.shortcuts import render, redirect
from django.urls import reverse
from .models import BadWord
from cadmin.decorators import staff_member_required

# Create your views here.

@staff_member_required(login_url='/login')
def badword_index(request):
    words = BadWord.objects.all()
    return render(request, 'badword/index.html', {'words': words})

@staff_member_required(login_url='/login')
def badword_create(request):
    if request.method == 'POST':
        badword = BadWord(text = request.POST['text'])
        badword.save()
        return redirect(reverse('badword_index'))
    return render(request, 'shared/not_found.html')

@staff_member_required(login_url='/login')
def badword_delete(request, id):
    if request.POST:
        word = BadWord.objects.get(pk = id)
        word.delete()
        return redirect(reverse('badword_index'))
    return render(request, 'shared/not_found.html')