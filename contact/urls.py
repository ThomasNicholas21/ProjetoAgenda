from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    # CRUD - Contact
    # CRUD - Read
    path('contact/<int:contact_id>/', views.contact, name='contact'),
    # CRUD - Create
    path('contact/create/', views.create, name='create'),
    # CRUD - UPDATE
    path('contact/<int:contact_id>/update/', views.update, name='update'),
    # CRUD - DELETE
    path('contact/<int:contact_id>/delete/', views.delete, name='delete'),

    # CRU - USER
    # CRUD - Read
    #path('contact/<int:contact_id>/', views.contact, name='contact'),
    # CRUD - Create
    path('user/create/', views.register, name='register'),
    # CRUD - UPDATE
    #path('contact/<int:contact_id>/update/', views.update, name='update'),
]