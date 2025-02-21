from django.shortcuts import render, redirect, get_object_or_404
from contact.models import Contact
from contact.forms import ContactForm
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='contact:login')
def create(request):
    form_action = reverse('contact:create')
    
    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES)
        context = {
            'form': form,
            'form_action': form_action,
        }

        # funcao que retorna true se o formulario
        # não retornar nenhum erro
        if form.is_valid():
            contact = form.save(commit=False)
            contact.owner = request.user
            contact.save()
            messages.success(request, 'Contato Cadastrado')
            return redirect('contact:contact', contact_id=contact.pk)


        return render(
                request,
                'contact/create.html',
                context
                )

    context = {
        'form': ContactForm(),
        'form_action': form_action,
    }

    return render(
        request,
        'contact/create.html',
        context
        )

# contact_id serve para trabalhar com URL dinâmica
@login_required(login_url='contact:login')
def update(request, contact_id):
    contact = get_object_or_404(
        Contact, pk=contact_id, show=True, owner=request.user
        )
    
    form_action = reverse(
        'contact:update', args=(contact_id,)
        )


    if request.method == "POST":
        # passa a instancia do formulario, para que ele altere a instancia 
        # que está sendo trabalhada
        form = ContactForm(request.POST, request.FILES, instance=contact)

        context = {
            'form': form,
            'form_action': form_action,
        }

        # funcao que retorna true se o formulario
        # não retornar nenhum erro
        if form.is_valid(): 
            contact = form.save(commit=False)
            contact.owner = request.user
            contact.save()
            messages.success(request, 'Contato Cadastrado')            
            return redirect('contact:contact', contact_id=contact.id)


        return render(
                request,
                'contact/create.html',
                context
                )

    context = {
        'form': ContactForm(instance=contact),
        'form_action': form_action,
    }

    return render(
        request,
        'contact/create.html',
        context
        )

@login_required(login_url='contact:login')
def delete(request, contact_id):
    contact = get_object_or_404(
        Contact, pk=contact_id, show=True, owner=request.user
        )
    
    confirmation = request.POST.get('confirmation', 'no')
    if confirmation == 'yes':
        contact.delete()
        return redirect('contact:index')

    context = {
        'contact': contact,
        'confirmation': confirmation,
    }
    return render(
        request,
        'contact/contact.html',
        context
        )
