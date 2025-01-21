# Django Framework

- Framework para desenvolvimento web de forma rápida, segura e escalável, que segue o padrão MVT (Model-View-Tamplate).

### MVT - Model-View-Template
- **Model:** vai gerarenciar a estrutura lógica de dados, mapeando os dados do manco de forma orientada a objeto.
- **View:** controla o que é exibido no navegador do usuário, manipulanto solicitações HTTP. Também pode enviar dados para dentro dos templates.
- **Template:** Define a apresentação visual dos dados, usando sistemas de templates do Django.

### HTTP Request (Requisição HTTP)
É a mensagem enviada do cliente (geralmente um navegador ou aplicativo) para o servidor para solicitar algum recurso, como uma página da web, um arquivo ou a execução de uma operação.

**Principais componentes de uma requisição HTTP:**
- Método HTTP: Indica a ação desejada:
    - GET: Solicita dados do servidor.
    - POST: Envia dados para o servidor.
    - PUT: Atualiza dados existentes.
    - DELETE: Remove dados no servidor.
- URL: O endereço do recurso solicitado.
- Cabeçalhos (Headers): Informações adicionais, como o tipo de conteúdo aceito (Accept), informações do cliente (User-Agent), etc.
- Corpo (Body): Dados enviados na requisição (aplicável para métodos como POST e PUT).

### HTTP Response (Resposta HTTP)
É a mensagem enviada pelo servidor ao cliente em resposta à requisição HTTP. Ela contém o resultado da solicitação, seja o conteúdo solicitado ou um status informando o que aconteceu.

- Principais componentes de uma resposta HTTP:
    - Código de status: Informa o resultado da requisição:
    - 200 OK: Sucesso.
    - 404 Not Found: Recurso não encontrado.
    - 500 Internal Server Error: Erro no servidor.
- Cabeçalhos (Headers): Informações sobre a resposta, como tipo de conteúdo (Content-Type), tamanho do conteúdo, etc.
Corpo (Body): O conteúdo da resposta, como o HTML de uma página, dados JSON, imagens, etc.

# Arquivos
## __settings.py:__ 
Toda a configuração da aplicação é feita nesse arquivo, definindo váriaveis de ambinete e configurações gerais para o funcionamento do aplicativo, como conexão com banco de dados, localização de templates, e detalhes de segurança.
- Configurações principais:
    - BASE_DIR
    - SECRET_KEY
    - DEBUG
    - ALLOWED HOSTS
- Aplicativos
    - INSTALLED_APPS
- Middlewares
    - MIDDLEWARE
- URLS E WSGI
    - ROOT_URLCONF
    - WSGI_APPLICATION
- Banco de dados
    - DATABASES
- Autentincação
    - AUTH_PASSORD_VALIDATORS
- Internacionalização
- Arquivos estáticos e mídia
    - STATIC_URL
    - STATIC_ROOT
    - STATICFILES_DIRS
    - MEDIA_URL/MEDIA_ROOT
- Outros
    - TEMPLATES
    - DEFAULT_AUTO_FIELD

# Comandos

### Iniciar projeto
```cmd
> django-admin startproject NomeProjeto
```
```cmd
>django-admin startproject NomeProjeto .
```

### Iniciar servidor
```cmd
>python manage.py runserver
```

### Iniciar um App
```cmd
>python manage.py startapp
```

### Coletar arquivos estáticos
Esse comando se utiliza quando a aplicação irá rodar em produção. Como Django não é um servidor, ele coleta e cria um diretório para que o mesmo seja configurado em um servidor. Para o mesmo funcionar, deve ser criado uma variável de ambiente STATIC_ROOT, indicando aonde esse diretório deve ser criado.
```cmd
>python manage.py collectstatic
```

# Conceitos
### namespace
Para evitar colisão de nomes iguais ao renderizar um arquivo HTML em tamplates, ou seja, evitar que dois templates com nome iguais sejam chamados de forma errada, se utiliza o __namespace__, no qual consiste em criar uma pasta dentro da pasta template para o arquivo em questão e declarar o seu caminho na view, exemplo: "templates/exemplo/exemplo.html". 

### URL Dinâmica
São URLs que vão incluir variáveis para definir rotas, permitindo que os valores sejam passados na URL e capturados na View correspondente. Evitando que crie URL estática para cada rota. Sendo ela configurada por padrão da seguinte maneira:
```python

# urls.py
urlpatterns = [
    path('exemplo/<exemplo:id>/', views.exemplo, name='exemplo')
]

# views.py
def exemplo(request, id):
    ...

```

# Django HTML
### extends
Herança de template utilizado.
```HTML
{% extends 'caminho.template' %}
```
### block & endblock
Faz trocar o valor do texto no template filho.
```HTML
{% block texto %} TEXTO {% endblock texto %}
```
### include
Utilizando juntamente a um "partials", normalmente utilizado quando está em partes, que pode ser utilizado em outro local.
```HTML
{% include 'caminho/partials/arquivo' %}
```

### load
Utilizar sempre que for utilizar arquivos staticos, irá carregar o aplicativo "django.contrib.staticfiles"
```HTML
{% load static %}
```

# Bibliotecas
### whitenoise
Servidor que pode ser utilizado para "servir" arquivos estáticos. Ele é um middleware que deve ser configurado na variável de ambiente MIDDLEWARE do django.
```cmd
>pip install whinoise
``` 
Colocar _"whitenoise.middleware.WhiteNoiseMiddleware",_ abaixo de middleware de segurança do Django.