# Configuração para Deploy no Render

## Configurações no Dashboard do Render

### 1. Build Settings
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`

### 2. Environment Variables
Configure estas variáveis no dashboard do Render:

```
DATABASE_URL=sqlite:///./test.db
SECRET_KEY=seu-secret-key-aqui
ALGORITHM=HS256
CORS_ORIGINS=*
ENVIRONMENT=production
```

### 3. Service Settings
- **Service Type**: Web Service
- **Environment**: Python 3
- **Region**: Escolha a mais próxima
- **Branch**: main (ou a branch que você está usando)

### 4. Health Check
- **Health Check Path**: `/health`

## Comandos para Testar Localmente

```bash
# Instalar dependências
pip install -r requirements.txt

# Executar teste simples
python test_simple.py

# Executar aplicação localmente
uvicorn main:app --host 0.0.0.0 --port 8000

# Testar endpoint de health
curl http://localhost:8000/health
```

## Troubleshooting

### Se o deploy falhar:
1. Verifique os logs no dashboard do Render
2. Teste localmente com: `python test_simple.py`
3. Verifique se todas as dependências estão no requirements.txt
4. Confirme que o start command está correto

### Se a aplicação não abrir:
1. Verifique se o serviço está "Running" no dashboard
2. Teste o endpoint `/health`
3. Verifique os logs de runtime
4. Confirme as variáveis de ambiente
