# 🚀 Deploy no Render - Guia Completo

## ❌ Problema Resolvido

O erro do Docker foi causado por versões específicas de pacotes que não estão disponíveis no Ubuntu.

## ✅ Solução Implementada

### 1. Dockerfile Simplificado

Criado `Dockerfile.simple` que:

- ✅ Usa apenas dependências básicas
- ✅ Não especifica versões específicas de pacotes
- ✅ Funciona no Render

### 2. Requirements Mínimos

Criado `requirements-minimal.txt` com versões estáveis.

## 🔧 Configuração no Render

### Build Settings:

```
Build Command: pip install -r requirements-minimal.txt
Start Command: uvicorn main:app --host 0.0.0.0 --port $PORT
```

### Environment Variables:

```
DATABASE_URL=sqlite:///./test.db
SECRET_KEY=seu-secret-key-aqui
ALGORITHM=HS256
CORS_ORIGINS=*
ENVIRONMENT=production
```

### Service Settings:

- **Service Type**: Web Service
- **Environment**: Python 3
- **Region**: Escolha a mais próxima
- **Branch**: main

## 🧪 Testar Localmente

### 1. Instalar dependências:

```bash
pip install -r requirements-minimal.txt
```

### 2. Testar aplicação:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

### 3. Testar Docker:

```bash
docker build -f Dockerfile.simple -t app:latest .
docker run -p 8000:8000 app:latest
```

## 📋 Checklist de Deploy

### Antes do Deploy:

- [ ] Executar `pip install -r requirements-minimal.txt`
- [ ] Testar `uvicorn main:app --host 0.0.0.0 --port 8000`
- [ ] Verificar se todos os arquivos estão commitados
- [ ] Confirmar configurações no Render

### No Render Dashboard:

- [ ] Build Command: `pip install -r requirements-minimal.txt`
- [ ] Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
- [ ] Variáveis de ambiente configuradas
- [ ] Health Check: `/health`

### Após Deploy:

- [ ] Verificar se serviço está "Running"
- [ ] Testar URL do Render
- [ ] Testar endpoint `/health`

## 🔍 Troubleshooting

### Se o build falhar:

1. Verificar logs no Render
2. Testar localmente com Docker
3. Verificar se requirements-minimal.txt está correto

### Se a aplicação não abrir:

1. Verificar se o serviço está "Running"
2. Testar endpoint `/health`
3. Verificar logs de runtime
4. Confirmar variáveis de ambiente

## 🎯 Comandos para Executar Agora

```bash
# 1. Instalar dependências
pip install -r requirements-minimal.txt

# 2. Testar localmente
uvicorn main:app --host 0.0.0.0 --port 8000

# 3. Se funcionar, fazer commit
git add .
git commit -m "Dockerfile simplificado e requirements mínimos"
git push

# 4. Configurar no Render com as configurações acima
```

## 📁 Arquivos Importantes

- ✅ `Dockerfile.simple` - Docker simplificado
- ✅ `requirements-minimal.txt` - Dependências mínimas
- ✅ `main.py` - Aplicação principal
- ✅ `.github/workflows/ci-cd.yml` - Pipeline atualizada

**Agora o deploy no Render deve funcionar perfeitamente!** 🎉
