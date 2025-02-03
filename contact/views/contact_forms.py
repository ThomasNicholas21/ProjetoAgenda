from django.shortcuts import render, redirect
from contact.forms import ContactForm

def create(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        context = {
            'form': form,
        }

        # funcao que retorna true se o formulario
        # não retornar nenhum erro
        if form.is_valid(): 
            form.save()
            return redirect('contact:create')


        return render(
                request,
                'contact/create.html',
                context
                )

    context = {
        'form': ContactForm(request.POST),
    }

    return render(
        request,
        'contact/create.html',
        context
        )
