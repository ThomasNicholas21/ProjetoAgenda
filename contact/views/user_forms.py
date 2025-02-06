from django.shortcuts import render
from contact.forms import RegisterForm
from django.contrib import messages

def register(request):
    form = RegisterForm()

    messages.info(request, 'texto qualquer')

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            # messages.success(request, 'Usuário Registrado')
    
    return render(
        request,
        'contact/register.html',
        {
            'form': form,
        }
    )
