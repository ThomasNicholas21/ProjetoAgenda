from django.shortcuts import render, get_object_or_404
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
    # single_contact = Contact.objects.\
    #     filter(pk=contact_id).\
    #     first()

    # if single_contact is None:
    #     raise Http404()

    # forma de levantar erro de página não encontrada
    # Filtra pelo PK e se show = True
    single_contact = get_object_or_404(
        Contact, pk=contact_id,
        show=True
        )

    context = {
        'contact': single_contact, 
    }

    return render(
        request,
        'contact/contact.html',
        context)
