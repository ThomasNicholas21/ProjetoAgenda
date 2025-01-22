from django.contrib import admin
from contact import models

# Register your models here.
# Configura os models dentro do painel administrativo do Django

# Função decoradora que permite registrar
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin): ...
