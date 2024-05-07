from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Bien
#from paypal.standard.forms import PayPalPaymentsForm
import uuid
#from django.urls import reverse


def index(request):
  biens = Bien.objects.order_by('-ajout_date').filter(est_disponible=True)
  paginator = Paginator(biens, 6)
  page = request.GET.get('page')
  paged_listings = paginator.get_page(page)

  context = {
    'biens': paged_listings
  }

  return render(request, 'biens/biens.html', context)

def bien(request, bien_id):
  bien = get_object_or_404(Bien, pk=bien_id)

  context = {
    'bien': bien,
  }

  return render(request, 'biens/bien.html', context)



def recherche(request):
  queryset_list = Bien.objects.order_by('-ajout_date')


  if 'cles' in request.GET:
    cles = request.GET['cles']
    if cles:
      queryset_list = queryset_list.filter(nom__icontains=cles)


  if 'ville' in request.GET:
    ville = request.GET['ville']  
    if ville:
      queryset_list = queryset_list.filter(ville__iexact=ville )


  if 'quartier' in request.GET:
    quartier = request.GET['quartier']
    if quartier:
      queryset_list = queryset_list.filter(quartier__iexact=quartier)

  context = {
    'biens': queryset_list,
    'values': request.GET
  }

  return render(request, 'biens/recherche.html', context)


#Payment Avec PayPal
def payment(request, bien_id):

    bien = Bien.objects.get(id=bien_id)

    host = request.get_host()

    paypal_checkout = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': bien.prix,
        'item_name': bien.nom,
        'invoice': uuid.uuid4(),
        'currency_code': 'XOF',
        'notify_url': f"http://{host}{reverse('paypal-ipn')}",
        'return_url': f"http://{host}{reverse('payment-success', kwargs = {'bien_id': bien_id})}",
        'cancel_url': f"http://{host}{reverse('payment-failed', kwargs = {'bien_id': bien_id})}",
    }

    paypal_payment = PayPalPaymentsForm(initial=paypal_checkout)

    context = {
        'bien': bien,
        'paypal': paypal_payment
    }

    #return render(request, 'biens/bien.html', context)


def PaymentSuccessful(request, bien_id):
    product = Product.objects.get(id=bien_id)
    return render(request, 'biens/succes.html', {'bien': bien})


def paymentFailed(request, bien_id):
    bien = Bien.objects.get(id=bien_id)
    return render(request, 'biens/echec.html', {'bien': bien})