from django.db import models
# modulo de utilitários
from django.utils import timezone

# Create your models here.

# O ID é criado de forma automática pelo Django.
# Model usado para criar o CRUD
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50)
    # blank torna um campo obrigatório ou não, porém não afeta na base de dados
    # EmailField() possui um validador de email
    email = models.EmailField(max_length=254, blank=True)
    # registra de forma automática o momento de criação
    created_date = models.DateTimeField(default=timezone.now)
    # TextField() não necessita de definir tamanho de caracter
    description = models.TextField(blank=True)
    # registra todos os contatos para estarem aparecendo
    show = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'