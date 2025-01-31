from django.shortcuts import render
from django.core.paginator import Paginator
from contact.models import Contact


def create(request):
    if request.method == 'POST':
        print(request.method)
        print(request.POST.get('first_name'))

    context = {

    }

    return render(
        request,
        'contact/create.html',
        context)
