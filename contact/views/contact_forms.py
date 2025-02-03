from django.shortcuts import render, redirect
from contact.forms import ContactForm
from django.urls import reverse

def create(request):
    form_action = reverse('contact:create')

    if request.method == "POST":
        form = ContactForm(request.POST)
        context = {
            'form': form,
            'form_action': form_action
        }

        # funcao que retorna true se o formulario
        # não retornar nenhum erro
        if form.is_valid(): 
            contact = form.save()
            return redirect('contact:update', contact_id=contact.pk)


        return render(
                request,
                'contact/create.html',
                context
                )

    form = ContactForm()
    context = {
        'form': form,
        'form_action': form_action
    }

    return render(
        request,
        'contact/create.html',
        context
        )

