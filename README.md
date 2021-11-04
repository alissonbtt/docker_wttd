# Eventex

Sistema de eventos 
## Como desenvolver:
1. Iniciar um repositório com GitHub.
2. Clonar o repositório.
3. Configurar as variáveis de ambientes.
4. Criar a uma imagem do container.
5. Criar e rodar o caontainer.


```
git init
git clone https://github.com/alissonbtt/docker_wttd.git
cp .env.sample .env
docker-compose build eventex
docker-compose up eventex
```

6. Para rodar navamente o conatainer, usar o seguinte comando para não excluir  o DB.

```
docker-compose up --no-deps -d
```

## Como fazer o deploy em uma instância ec2 aws com linux

### Após criar e ter acesso a instância ec2, executar os seguintes comando no CLI

1. Instalar o GIT.
2. Instalar o Docker.
3. Configurar o docker para iniciar sempre que a máquina for reiniciada
4. Iniciar o Docker
5. Dar permissão para que o usuário gerencia containers
6. Instalar o docker compose
7. Aplicar permissões ao executavel binário
8. Reiniciar instância.
```
sudo yum install git -y
sudo amazon-linux-extras install docker -y
sudo systemctl enable docker.service
sudo systemctl start docker.service
sudo usermod -aG docker ec2-user
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo reboot
```
### Após reiniciar a instância, rodar os seguintes passos.

9. Clonar o repositório do projeto
10. Entrar na pasta do projeto.
11. Copiar o arquivo .env.sample para o arquivo .env
12. Abrir ao arquivo .env e alterarr as varáveis de ambiente
DB_NAME=nome_do_db
DB_USER=nome_usuário
DB_PASS=senha_db
SECRET_KEY=senha_secretkey_django
ALLOWED_HOSTS=DNS_IPv4_público_da instância
DEFAULT_FROM_EMAIL=email_criado_sendrig
EMAIL_HOST_PASSWORD=configurar_email_senha_sendgrid

```
git clone https://github.com/alissonbtt/docker_wttd.git
cd docker_wttd
cp .env.sample .env
vi .env
```
13. Após ajustar as variáveis de ambiente, gerar uma imágem com docker
14. Criar e rodar containers

```
docker-compose -f docker-compose-deploy.yml build eventex
docker-compose -f docker-compose-deploy.yml up -d
```

15. Caso necessário, atualizar o código se hover alterações.
16. Atualizar a imagem do container.
17. Rodar novamente o docker compose sem excluir o Banco de dados.

``` 
git pull origin
docker-compose -f docker-compose-deploy.yml build eventex
docker-compose -f docker-compose-deploy.yml up --no-deps -d eventex
```