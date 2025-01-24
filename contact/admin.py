from django.contrib import admin
from contact import models

# Register your models here.
# Configura os models dentro do painel administrativo do Django

# Função decoradora que permite registrar
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin): 
    list_display = 'name',
    ordering = 'name'

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    # permite criar uma coluna para o painel administrativo
    list_display = 'id', 'first_name', 'last_name', 'phone', 'description', 'show'
    # permite ordenar as colunas de forma crescente e descrescente
    ordering = '-id',
    # permite criar filtros
    list_filter = 'created_date',
    # permite criar barra de pesquisa
    search_fields = 'id', 'first_name', 'last_name'
    # cria uma paginação, permitindo controlar quantidade
    # de objetos criados
    #list_per_page = 1
    # definie o máximo de objetos mostrado em uma página só
    list_max_show_all = 50
    # permite a edição sem a necessidade de acessar a url
    list_editable = 'last_name',
    # permite acessar a url pelas variavéis definidas
    # OBS: não é possível deixar uma variável como editável 
    # e acessível por link.
    list_display_links = 'first_name',