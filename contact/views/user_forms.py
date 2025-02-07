from django.shortcuts import render, redirect
from django.urls import reverse
from contact.forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

def register(request):
    form_action = reverse('contact:register')

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário Registrado')
            return redirect('contact:index')
    
    return render(
        request,
        'contact/register.html',
        {
            'form': RegisterForm(),
            'form_action': form_action,
        }
    )

def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
    

    context = {
        'form': form
    }
    return render(
        request,
        'contact/login.html',
        context
    )

def logout_view(request):
    auth.logout(request)
    return redirect('contact:login')

