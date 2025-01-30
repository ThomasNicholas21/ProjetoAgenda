from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    # CRUD - Read
    path('contact/<int:contact_id>/detail/', views.contact, name='contact'),
    # CRUD - Create
    path('contact/<int:contact_id>/create/', views.contact, name='contact'),
]