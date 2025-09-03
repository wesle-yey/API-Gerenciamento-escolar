# 🐳 Configuração do Docker Hub para CI/CD

## Passos para configurar o Docker Hub:

### 1. Criar conta no Docker Hub
- Acesse [hub.docker.com](https://hub.docker.com)
- Crie uma conta gratuita

### 2. Criar repositório
- Clique em "Create Repository"
- Nome: `gerenciamento-escolar`
- Descrição: "Sistema de Gerenciamento Escolar com FastAPI"
- Visibilidade: Public ou Private

### 3. Gerar Access Token
- Vá em Account Settings > Security
- Clique em "New Access Token"
- Nome: `github-actions`
- Permissões: Read & Write
- Copie o token gerado

### 4. Configurar Secrets no GitHub
No seu repositório GitHub:

1. Vá em Settings > Secrets and variables > Actions
2. Clique em "New repository secret"
3. Adicione:
   - `DOCKERHUB_USERNAME`: seu usuário do Docker Hub
   - `DOCKERHUB_TOKEN`: o token gerado no passo 3

## Como usar:

Após configurar, o pipeline irá:
1. Executar testes automaticamente
2. Fazer build da imagem Docker
3. Publicar no Docker Hub com tags:
   - `latest`: versão mais recente
   - `{commit-hash}`: versão específica

## Executar localmente:

```bash
# Baixar e executar
docker pull seu_usuario/gerenciamento-escolar:latest
docker run -p 8000:8000 seu_usuario/gerenciamento-escolar:latest

# Ou usar docker-compose
docker-compose up -d
```

## Verificar status:

- Acesse: http://localhost:8000
- Login padrão: crie um usuário via `/register`
