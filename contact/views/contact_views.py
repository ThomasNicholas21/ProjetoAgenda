from django.shortcuts import render
from contact.models import Contact
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
    singles_contact = Contact.objects.get(pk=contact_id)

    context = {
        'contact': singles_contact, 
    }

    return render(
        request,
        'contact/contact.html',
        context)
