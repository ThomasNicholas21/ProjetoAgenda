<h1 align="center">
  📞 Agenda Telefônica - Django
</h1>

## :rocket: Sobre o projeto

Este é um projeto desenvolvido para aprofundar conhecimentos no framework Django, explorando conceitos fundamentais como:

- Configuração do ambiente e estrutura de um projeto Django;
- Uso de URLs dinâmicas para navegação eficiente;
- Definição de `models` para manipulação de dados no banco de dados;
- Configuração do painel administrativo para gerenciar contatos;
- Implementação de `views` para controle das lógicas da aplicação;
- Uso de `forms` para cadastro e edição de contatos;
- Sistema de autenticação de usuário integrado ao Django;
- Utilização de `Django Templates` para renderização dinâmica de páginas.

## :gear: Tecnologias utilizadas

- **Django**: Framework web principal da aplicação;
- **SQLite** (ou outro banco compatível) para armazenamento dos dados;
- **HTML & CSS** para a interface;

## :clipboard: Funcionalidades

- Cadastro, edição e remoção de contatos;
- Pesquisa de contatos por nome ou telefone;
- Autenticação de usuário para acesso ao sistema;
- Gerenciamento de contatos via painel administrativo do Django.

## :hammer: Como executar o projeto

1. Clone o repositório:
```bash
$ git clone https://github.com/seu-usuario/agenda-telefonica.git
$ cd agenda-telefonica
```

2. Crie um ambiente virtual e instale as dependências:
```bash
$ python -m venv venv
$ source venv/bin/activate  # Linux/Mac
$ venv\Scripts\activate  # Windows
$ pip install -r requirements.txt
```

3. Configure o banco de dados:
```bash
$ python manage.py migrate
```

4. Crie um superusuário para acessar o painel administrativo:
```bash
$ python manage.py createsuperuser
```

5. Inicie o servidor:
```bash
$ python manage.py runserver
```

6. Acesse a aplicação no navegador:
```
http://127.0.0.1:8000/
```

## :lock: Autenticação de usuários
O sistema utiliza o próprio sistema de autenticação do Django, permitindo que apenas usuários autenticados gerenciem contatos.

## :notebook: Anotações adicionais
Para mais detalhes sobre o aprendizado durante o desenvolvimento deste projeto, consulte minhas [anotações](https://github.com/ThomasNicholas21/ProjetoAgenda/tree/master/anotacoes).

---
