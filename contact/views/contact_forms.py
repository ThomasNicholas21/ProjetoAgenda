from django.shortcuts import render
from django.core.paginator import Paginator
from contact.models import Contact
from django import forms

class ContactForm(forms.ModelForm):
    class Meta: 
        # define qual model esse form se refere
        model = Contact
        fields = ('first_name', 'last_name', 'phone',)

def create(request):

    context = {
        'form': ContactForm(),
    }

    return render(
        request,
        'contact/create.html',
        context)
