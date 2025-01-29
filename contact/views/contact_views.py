from django.shortcuts import render
from contact.models import Contact
from django.http import Http404
# Create your views here.

def index(request):
    contacts = Contact.objects.\
        filter(show=True).\
        order_by('-id')[:10]
    
    # Mostra como o django realiza 
    print(contacts.query)

    context = {
        'contacts': contacts, 
    }

    return render(
        request,
        'contact/index.html',
        context)


def contact(request, contact_id):
    singles_contact = Contact.objects.\
        filter(pk=contact_id).\
        first()

    if singles_contact is None:
        raise Http404()

    context = {
        'contact': singles_contact, 
    }

    return render(
        request,
        'contact/contact.html',
        context)
