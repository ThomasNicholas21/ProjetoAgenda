from django.db import models
# modulo de utilitários
from django.utils import timezone

# Create your models here.

# O ID é criado de forma automática pelo Django.
# Model usado para criar o CRUD
class Category(models.Model):
    class Meta:
        # sempre quando procura o singular desse model
        # será 'Category'
        verbose_name = 'Category'

    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'

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
    # registra atributos de imagens de forma não obrigatória
    # especifíca o caminho de upload.
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/%d')
    # isso é uma chave estrangeira, logo deve-se criar o novo model
    # on_delete - parametro que define se o contato será apagado caso a categoria for.
    # models.CASCADE - deleta todos os contatos que possue a categoria
    # models.SET_NULL - quando delete a categoria, o contato fica como null
    # Descrição - A categoria não é obrigatória, pode ser nula, e caso for apagada
    # o contato não é apagado, e sua categoria ficará nula.
    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    