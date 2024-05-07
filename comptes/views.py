from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact



# Fonction pour gérer les inscriptions
def inscription(request):
  if request.method == 'POST':
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    if password == password2:
      if User.objects.filter(username=username).exists():
        messages.error(request, 'Ce nom d\'utilisateur est déjà pris')
        return redirect('inscription')
      else:
        if User.objects.filter(email=email).exists():
          messages.error(request, 'Cet e-mail est utilisé')
          return redirect('inscription')
        else:
          user = User.objects.create_user(username=username, password=password,email=email, first_name=first_name, last_name=last_name)
          user.save()
          messages.success(request, 'Vous êtes maintenant inscrit et pouvez vous connecter')
          return redirect('connexion')
    else:
      messages.error(request, 'Les mots de passe ne correspondent pas')
      return redirect('inscription')
  else:
    return render(request, 'comptes/inscription.html')




# Fonction pour gérer les connexions
def connexion(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None:
      auth.login(request, user)
      messages.success(request, 'Vous êtes maintenant connecté')
      return redirect('dashboard')
    else:
      messages.error(request, 'les informations d\'identification sont invalides')
      return redirect('connexion')
  else:
    return render(request, 'comptes/connexion.html')



# Fonction pour gérer les deconnexions
def deconnexion(request):
  if request.method == 'POST':
    auth.logout(request)
    messages.success(request, 'Vous êtes maintenant déconnecté')
    return redirect('index')



# Le tableau de board utilisateur
def dashboard(request):
  user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)

  context = {
    'contacts': user_contacts
  }
  return render(request, 'comptes/dashboard.html', context)