from django.contrib import admin
from contact import models

# Register your models here.
# Configura os models dentro do painel administrativo do Django

# Função decoradora que permite registrar
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    # permite criar uma coluna para o painel administrativo
    list_display = 'id', 'first_name', 'last_name', 'phone', 'description'
    # permite ordenar as colunas de forma crescente e descrescente
    ordering = '-id',
    # permite criar filtros
    list_filter = 'created_date',