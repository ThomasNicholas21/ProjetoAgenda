from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    # CRUD - Contact
    # CRUD - Read
    path('contact/<int:contact_id>/', views.contact, name='contact'),
    # CRUD - Create - Login Required
    path('contact/create/', views.create, name='create'),
    # CRUD - UPDATE - Login Required
    path('contact/<int:contact_id>/update/', views.update, name='update'),
    # CRUD - DELETE - Login Required
    path('contact/<int:contact_id>/delete/', views.delete, name='delete'),

    # CRU - USER
    # CRUD - Read
    #path('contact/<int:contact_id>/', views.contact, name='contact'),
    # CRUD - Create
    path('user/create/', views.register, name='register'),
    #path('contact/<int:contact_id>/update/', views.update, name='update'),
    path('user/login/', views.login_view, name='login'),
    # Login Required
    path('user/logout/', views.logout_view, name='logout'),
    # CRUD - UPDATE - Login Required
    path('user/update/', views.update_view, name='user_update'),
]