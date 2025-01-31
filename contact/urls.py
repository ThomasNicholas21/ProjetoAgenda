from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    # CRUD - Read
    # path('contact/<int:contact_id>/detail/', views.contact, name='contact'),
    # CRUD - Create
    path('contact/create/', views.create, name='create'),
    # CRUD - UPDATE
    # path('contact/<int:contact_id>/update/', views.contact, name='contact'),
    # CRUD - DELETE
    # path('contact/<int:contact_id>/delete/', views.contact, name='contact'),
]