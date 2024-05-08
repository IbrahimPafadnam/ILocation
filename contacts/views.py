from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact
from django.conf import settings

def contact(request):
  if request.method == 'POST':
    bien_id = request.POST['bien_id']
    bien = request.POST['bien']
    nom = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']
    user_id = request.POST['user_id']
    agent = request.POST['agent_email']

    if request.user.is_authenticated:
      user_id = request.user.id
      has_contacted = Contact.objects.all().filter(bien_id=bien_id, user_id=user_id)
      if has_contacted:
        messages.error(request, 'Vous avez déjà fait une demande pour cette annonce')
        return redirect('/biens/'+bien_id)
      
      contact = Contact(bien=bien, bien_id=bien_id, nom=nom, email=email, phone=phone, message=message, user_id=user_id )
      contact.save()

      send_mail(
        subject='ILocation: Contact de '+ nom + ' pour ' + bien,
        message=nom + ' vous a contacté concernant le bien '+bien+ ' .Son numéro de téléphone est le '+phone+ ' .Connectez-vous au panneau d\'administration pour plus d\'informations.',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[agent,'ipafadnam10@gmail.com'],
        fail_silently=False
      )

      messages.success(request, 'Votre demande a été soumise, un agent vous répondra bientôt')
      return redirect('/biens/'+bien_id)
    
    messages.error(request, 'Veillez vous connecter')
    return redirect('connexion')
  
    
    

