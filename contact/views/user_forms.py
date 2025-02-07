from django.shortcuts import render, redirect
from django.urls import reverse
from contact.forms import RegisterForm, RegisterUpdteForm
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
            return redirect('contact:login')
    
    return render(
        request,
        'contact/register.html',
        {
            'form': RegisterForm(),
            'form_action': form_action,
        }
    )

def update_view(request):
    form = RegisterUpdteForm(instance=request.user)
    
    return render(
        request,
        'contact/register.html',
        {
            'form': form,
        }
    )

def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Logado com sucesso!')
            return redirect('contact:index')
        
        messages.error(request, 'Login Inválido')
    

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
    messages.success(request, 'Usuário deslogado')
    return redirect('contact:login')

