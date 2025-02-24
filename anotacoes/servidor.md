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