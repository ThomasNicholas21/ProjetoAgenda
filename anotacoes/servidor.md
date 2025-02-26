# Passo a passo para primeiro Deploy VM
## VM
Uma Máquina Virtual (VM) é um ambiente de computação simulado que executa um sistema operacional e aplicativos como se fosse um computador físico. Ela é criada e gerenciada por um software chamado hypervisor, permitindo que vários sistemas operacionais rodem simultaneamente no mesmo hardware.
### **tipo de hypervisor**
Hypervisor é um software responsável por gerenciar as maquinas virtuais, permitindo compartilhar recursos do hardware físico. Sendo dividos em _bare metal_, que não necessita de um sistema operacional intermediário, e Hosted, que executa em um sistema operacional.

### Imagem VM
Uma __imagem__ normalmente contem um sistema operacional e configurações. Necessário baixar ISO do Ubunto.

### Virtualização, armazenamento e Snapshots
- Virtualização: A virtualização dos hardwares, permite que a VM tenha acesso de hardwares, podendo ser controlada pelo Hypervisor.
- Armazenamento: A Vm utiliza discos virutal que simulam HD físicos.
- Snapshots: Forma de mostrar o estado atual da VM para que possa ser restaurada.

### Tipos de Virtualização
- **Virtualização Completa**
    - O hypervisor emula completamente o hardware para que o sistema operacional convidado funcione sem modificações.

- **Paravirtualização**
    - O SO convidado é modificado para se comunicar diretamente com o hypervisor, reduzindo a sobrecarga e aumentando a eficiência.

- **Virtualização de Armazenamento**
    - Permite abstrair diferentes dispositivos de armazenamento para as VMs, criando um pool de discos virtuais.

- **Virtualização de Rede**
    - Criação de redes virtuais dentro do hypervisor para isolar, conectar ou simular redes físicas.

- **Containers vs. VMs**
    - Os containers (exemplo: Docker, LXC) são uma forma de virtualização mais leve que compartilha o mesmo kernel do SO, diferente das VMs que possuem um SO completo.

## VirtualBox
Necessário estar configurado, como Rede (modo bridge), configuração de mémoria RAM cpu. As configurações variam de acordo com cada interesse.

## Ubuntu
Ao instalar, juntamente a ISO, algumas dependências são necessárias na instalação, como:
```cmd
>sudo apt upgrade
>sudo apt install build-essentials gcc make perl dkms curl
Opcional
>sudo apt install git
```
## SSH
### Primeiro passo
Necessário instalar o SSH e realizar as seguintes configurações:
```cmd
sudo apt install ssh
```
Depois configurar o SSH, para senhas e tentativas de autenticação (opcional):
```cmd
>sudo nano etc/ssh/sshd_config
```
Procurar por PasswordAuthentication e MaxAuthTries (configurar de acordo com a aplicação)

### Segundo passo
Após realizar a configuração, é necessário gerar as chaves, privada e pública, fora da máquina virtual
```cmd
> ssh-keygen -t rsa -b 4096 -C "comentario_chave"
```
Depois de realizar esse comando é solicitado o caminho e senha (opcional). Após gerar as chaves, insira a chave pública no servidor:
```cmd
> nano ~/.ssh/authorized-keys
```
Salve apertando ctrl O e feche apertando ctrl X.


## Configurar Django:
Para configurar o Django, primeiramente é necessário criar arquivo local_host.py, aonde irá configurar SECRET_KEY, ALOWWED_HOSTS e DATABASES.
Para gerar uma secret key:
```python
# python -c "import string as s;from secrets import SystemRandom as SR;print(''.join(SR().choices(s.ascii_letters + s.digits + s.punctuation, k=64)));"
```


## Configurar Servidor:
Para conectar no servidor:
```cmd
ssh user@ip_server
```

Comando iniciais:
```cmd
>sudo apt update -y
```
```cmd
>sudo apt upgrade -y
```
```cmd
>sudo apt autoremove -y
```
```cmd
>sudo apt install build-essential -y
```
Para instalar Python
```cmd
>sudo add-apt-repository ppa:deadsnakes/ppa
```
```cmd
>sudo apt install python3.11 python3.11-venv
```
Para Instalar Servidor:
```cmd
>sudo apt install nginx -y
```
```cmd
>sudo apt install certbot python3-certbot-nginx -y
```
```cmd
>sudo apt install postgresql postgresql-contrib -y
```
```cmd
>sudo apt install libpq-dev -y
```
```cmd
>sudo apt install git -y
```

### Configurando GIT
Configuração inicial Git:
```cmd
>git config --global user.name 'Seu nome'
>git config --global user.email 'seu_email@gmail.com'
```

Criação do repostiório no servidor:
```cmd
>mkdir ~/agendarepo ~/agendaapp
```

Configurando reporsitório bare:
```cmd
>cd ~/agendarepo
>git init --bare
```

Configurando repositório:
```cmd
>cd ~/agendaapp
>git init
>git remote add agendarepo ~/agendarepo
```

__Computador Local__
```cmd
>git remote add agendarepo usuario@IP_SERVIDOR:~/agendarepo
>git push agendarepo master
```

__Servidor__
```cmd
>cd ~/agendaapp
>git pull agendarepo main
```

### Configurando Base de Dados para servidor (Nesse caso, foi utilizado Postgresql)
```cmd
sudo -u postgres psql

# Copie de acordo com a configuração local_settings.py
postgres=# create role usuario_agenda with login superuser createdb createrole password 'senha_usuario_agenda';
CREATE ROLE
postgres=# create database projeto_agenda with owner usuario_agenda;
CREATE DATABASE
postgres=# grant all privileges on database projeto_agenda to usuario_agenda;
GRANT
postgres=# \q

sudo systemctl restart postgresql
```

### Criar o local_settings.py no servidor:
Ao acessar o editor de texto do Servidor, cole as configurações feitas para o database, salve com ctrl O e depois saia com ctrl X.
```cmd
nano ~/agendaapp/project/local_settings.py

```

### Configurar Django no Servidor
Deve-se instalar as depndências do projetos (requirements.txt), e também as seguintes bibliotecas:
```cmd
pip install gunicorn
pip install psycopg
```

Depois realizar a configuração do Django:
```cmd
python manage.py runserver
python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuser
```
_OBS_: Crie senha de usuário forte!!

### Configurando o gunicorn para rodar a aplicação:
Para configurar o gunicorn, crie o arquivo socket e configure:
```txt
# Criando o arquivo __GUNICORN_FILE_NAME__.socket
sudo nano /etc/systemd/system/__GUNICORN_FILE_NAME__.socket

Coloque este contéudo no arquivo
[Unit]
Description=gunicorn __GUNICORN_FILE_NAME__ socket

[Socket]
ListenStream=/run/__GUNICORN_FILE_NAME__.socket

[Install]
WantedBy=sockets.target
```
Agora configure o serviço:
```txt
# Criando o arquivo __GUNICORN_FILE_NAME__.service
sudo nano /etc/systemd/system/__GUNICORN_FILE_NAME__.service

# Conteúdo do arquivo service
[Unit]
Description=Gunicorn daemon (You can change if you want)
Requires=__GUNICORN_FILE_NAME__.socket
After=network.target

[Service]
User=__YOUR_USER__
Group=www-data
Restart=on-failure
# EnvironmentFile=/home/__YOUR_USER__/__APP_ROOT_NAME__/.env
WorkingDirectory=/home/__YOUR_USER__/__APP_ROOT_NAME__
# --error-logfile --enable-stdio-inheritance --log-level and --capture-output
# are all for debugging purposes.
ExecStart=/home/__YOUR_USER__/__APP_ROOT_NAME__/venv/bin/gunicorn \
          --error-logfile /home/__YOUR_USER__/__APP_ROOT_NAME__/gunicorn-error-log \
          --enable-stdio-inheritance \
          --log-level "debug" \
          --capture-output \
          --access-logfile - \
          --workers 6 \
          --bind unix:/run/__GUNICORN_FILE_NAME__.socket \
          __WSGI_FOLDER_NAME__.wsgi:application

[Install]
WantedBy=multi-user.target

```

__Comandos__
```txt
# Ativando
sudo systemctl start __GUNICORN_FILE_NAME__.socket
sudo systemctl enable __GUNICORN_FILE_NAME__.socket

# Checando
sudo systemctl status __GUNICORN_FILE_NAME__.socket
curl --unix-socket /run/__GUNICORN_FILE_NAME__.socket localhost
sudo systemctl status __GUNICORN_FILE_NAME__

# Restarting
sudo systemctl restart __GUNICORN_FILE_NAME__.service
sudo systemctl restart __GUNICORN_FILE_NAME__.socket
sudo systemctl restart __GUNICORN_FILE_NAME__

# After changing something
sudo systemctl daemon-reload

# Debugging
sudo journalctl -u __GUNICORN_FILE_NAME__.service
sudo journalctl -u __GUNICORN_FILE_NAME__.socket
```

__Variáveis__
```txt
# __GUNICORN_FILE_NAME__ the name of the gunicorn file you want
# __YOUR_USER__ your user name
# __APP_ROOT_NAME__ the folder name of your project
# __WSGI_FOLDER_NAME__ the folder name where you find a file called wsgi.py
```


### Configurando _nginx_
Para configurar necessário colocar de acordo com ambiente de configuração. Acesse o diretório:
```cmd
>etc/nginx/sites-enable
```
Nele terá um arquivo dafault que pode ser excluido da seguinte maneira:
```cmd
>sudo rm -f __nome_do_arquivo__
```
Ao excluir acesse:
```cmd
>etc/nginx/sites-available
```
Crie um arquivo chamado agenda com seguinte conteudo:
```cmd
>sudo nano agenda
```
Conteudo:
```txt
server {
  listen 80;
  listen [::]:80;
  server_name __YOUR_DOMAIN_OR_IP__;

  # Add index.php to the list if you are using PHP
  index index.html index.htm index.nginx-debian.html index.php;
  
  # ATTENTION: __STATIC_ABSOLUTE_PATH__
  location /static {
    autoindex on;
    alias __STATIC_ABSOLUTE_PATH__;
  }

  # ATTENTION: __MEDIA_ABSOLUTE_PATH__ 
  location /media {
    autoindex on;
    alias __MEDIA_ABSOLUTE_PATH__;
  }

  # ATTENTION: __GUNICORN_FILE_NAME__
  location / {
    proxy_pass http://unix:/run/__GUNICORN_FILE_NAME__.socket;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection 'upgrade';
    proxy_set_header Host $host;
    proxy_cache_bypass $http_upgrade;
  }

  # deny access to .htaccess files, if Apache's document root
  # concurs with nginx's one
  #
  location ~ /\.ht {
    deny all;
  }

  location ~ /\. {
    access_log off;
    log_not_found off;
    deny all;
  }

  gzip on;
  gzip_disable "msie6";

  gzip_comp_level 6;
  gzip_min_length 1100;
  gzip_buffers 4 32k;
  gzip_proxied any;
  gzip_types
    text/plain
    text/css
    text/js
    text/xml
    text/javascript
    application/javascript
    application/x-javascript
    application/json
    application/xml
    application/rss+xml
    image/svg+xml;

  access_log off;
  #access_log  /var/log/nginx/__YOUR_DOMAIN_OR_IP__-access.log;
  error_log   /var/log/nginx/__YOUR_DOMAIN_OR_IP__-error.log;
}
```

__variáveis__
```txt
# REPLACES
# __YOUR_DOMAIN_OR_IP__ = Replace with your domain
# __APP_ABSOLUTE_PATH__ = Replace with the path to the folder for the project
# __STATIC_ABSOLUTE_PATH__ = Replace with the path to the folder for static files
# __MEDIA_ABSOLUTE_PATH__ = Replace with the path to the folder for media files
# __GUNICORN_FILE_NAME__ = Replace with your unix socket name (don't add .socket)
```

Depois disso crie um link para site-enable da seguinte maneira:
```cmd 
> sudo ln -s etc/nginx/sites-available/agenda etc/nginx/sites-enable
```

# Como fazer alterações com git, gunicorn e nginx
## git
Ao fazer alteração local, necessário fazer o push para o repositório bare configurado no servidor, nesse caso seria:
```cmd
>git push agendarepo master
```
OBS: Antes de realizar o push, é interessante verificar se o repositório do servidor está sincronizado com repositório bare, realizando:
```cmd
>git status
>git add .
>git commit -m "texto"
>git push agendarepo master
```

Depois de realizar o push para agendarepo do ambiente de desenvolvimento local é necessário realizar um pull no repositório em produção:
```cmd
>git pull agendarepo master
```

## gunicorn
Necessário realizar o restart do servidor configurado com gunicorn.
```cmd
>sudo systemctl restart agenda
```
## nginx
Necessário realizar o restart do servidor configurado com gunicorn.
```cmd
>sudo systemctl restart nginx
```

