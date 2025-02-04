from django.shortcuts import render, redirect, get_object_or_404
from contact.models import Contact
from contact.forms import ContactForm
from django.urls import reverse

def create(request):
    form_action = reverse('contact:create')

    if request.method == "POST":
        form = ContactForm(request.POST)
        context = {
            'form': form,
            'form_action': form_action,
        }

        # funcao que retorna true se o formulario
        # não retornar nenhum erro
        if form.is_valid():
            contact = form.save()
            return redirect('contact:update', contact_id=contact.id)


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
def update(request, contact_id):
    contact = get_object_or_404(
        Contact, pk=contact_id, show=True
        )
    
    form_action = reverse(
        'contact:update', args=(contact_id,)
        )


    if request.method == "POST":
        # passa a instancia do formulario, para que ele altere a instancia 
        # que está sendo trabalhada
        form = ContactForm(request.POST, instance=contact)

        context = {
            'form': form,
            'form_action': form_action,
        }

        # funcao que retorna true se o formulario
        # não retornar nenhum erro
        if form.is_valid(): 
            contact = form.save()
            return redirect('contact:update', contact_id=contact.id)


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

def delete(request, contact_id):
    contact = get_object_or_404(
        Contact, pk=contact_id, show=True
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