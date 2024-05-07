from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Commentaire
from .forms import CommentaireForm

def commentaire(request):
    commentaires = Commentaire.objects.order_by('-date_creation')
    if request.method == 'POST':
        form = CommentaireForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        messages.error(request, 'Merci de nous laisser un commentaire')
        return redirect('avis')
    else:
        form = CommentaireForm()

    context = {
    'form': form,
    'commentaires':commentaires,
    }
    
    return render(request, 'commentaire/avis.html', context)
