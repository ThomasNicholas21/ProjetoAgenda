from django.shortcuts import render
from django.urls import reverse
from contact.forms import RegisterForm
from django.contrib import messages

def register(request):
    form_action = reverse('contact:register')

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário Registrado')
    
    return render(
        request,
        'contact/register.html',
        {
            'form': RegisterForm(),
            'form_action': form_action,
        }
    )
