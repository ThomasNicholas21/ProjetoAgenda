import os
import sys
from datetime import datetime
from pathlib import Path
from random import choice

import django
from django.conf import settings

# Faz com que pegue informações de pastas fora de utils
# sendo elas do escopo do projeto django
DJANGO_BASE_DIR = Path(__file__).parent.parent
NUMBER_OF_OBJECTS = 1000

# Faz com que inclua no sistema do python o escopo do projeto
# para que ele procure informaçoes dentro do projeto
sys.path.append(str(DJANGO_BASE_DIR))
# sempre quando utilizar django sem ser por manage.py é necessário
# definir variável de ambiente para apontar aonte está as configurações
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'
settings.USE_TZ = False

django.setup()

if __name__ == "__main__":
    import faker
    # realizando importação após configuração para evitar erro
    from contact.models import Contact, Category

    # objects é o gerenciador dos models, dessa forma será deletado
    # todos os contatos existentes.
    Contact.objects.all().delete()
    Category.objects.all().delete()

    # definindo linguagem
    fake = faker.Faker('pt_BR')
    categories = ['Amigos', 'Familia', 'Conhecidos']

    # crias as categorias
    django_catogories = [Category(name=name) for name in categories]

    # cria na base de dados as categorias definidas
    for category in django_catogories:
        category.save()

    django_contacts = []
    
    for _ in range(NUMBER_OF_OBJECTS):
        # criando perfis aleatorios e extraindo infos
        profile = fake.profile() 
        first_name, last_name = profile['name'].split(' ', 1)
        phone = fake.phone_number()
        email = profile['mail']
        created_date: datetime = fake.date_this_year()
        description = fake.text(max_nb_chars=100)
        category = choice(django_catogories)

        django_contacts.append(
            Contact(
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                email=email,
                created_date=created_date,
                description=description,
                category=category,
            )
        )
    
    if len(django_contacts) > 0:
        # bulk create cria varios contatos de uma vez
        Contact.objects.bulk_create(django_contacts)
