from django.shortcuts import render
from django.core.paginator import Paginator
from contact.models import Contact


def create(request):
    value = request.POST.get('first_name')
    print(value)

    context = {

    }

    return render(
        request,
        'contact/create.html',
        context)
