from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from contact.models import Contact
from django.contrib.auth.decorators import login_required

@login_required(login_url='contact:login')
def index(request):
    contacts = Contact.objects\
        .filter(show=True)\
        .filter(owner=request.user)\
        .order_by('-id')
    
    paginator = Paginator(contacts, 10)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    
    # Mostra como o django realiza 
    # print(contacts.query)

    context = {
        "page_obj": page_obj,
        'title' : 'Contatos - ',
    }

    return render(
        request,
        'contact/index.html',
        context)


def search(request):
    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('contact:index')

    # utilizando field look ups
    # https://docs.djangoproject.com/en/4.2/ref/models/querysets/#field-lookups
    # classe Q permite separar as buscas e utilizar variável "or" com " | "
    contacts = Contact.objects.\
        filter(show=True).\
        filter(
            Q(first_name__icontains=search_value) |
            Q(last_name__icontains=search_value) |
            Q(phone__icontains=search_value) |
            Q(email__icontains=search_value)
            ).\
        order_by('-id')

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    # verificando query criada
    #print(contacts.query)

    context = {
        'page_obj': page_obj, 
        'title' : 'Contatos - ',
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

    contact_name = f'{single_contact.first_name} {single_contact.last_name} -'

    context = {
        'contact': single_contact,
        'title': contact_name
    }

    return render(
        request,
        'contact/contact.html',
        context)
