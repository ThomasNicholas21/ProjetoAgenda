from django.shortcuts import render
from django.core.paginator import Paginator
from contact.models import Contact
from django import forms
from django.core.exceptions import ValidationError

class ContactForm(forms.ModelForm):
    class Meta: 
        # define qual model esse form se refere
        model = Contact
        fields = ('first_name', 'last_name', 'phone',)

    # pega os dados do formulário
    def clean(self):
        cleaned_data = self.cleaned_data
        
        self.add_error(
            'first_name',
            ValidationError(
                'Erro',
                code='invalid'
            )
        )

        return super().clean()

def create(request):
    if request.method == "POST":
        context = {
            'form': ContactForm(request.POST),
        }

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
