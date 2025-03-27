# Usa uma imagem Python oficial como base
FROM python:3.9-slim

WORKDIR /app

# Instala dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da aplicação
COPY . .

# Expõe a porta da API
EXPOSE 8000

# Comando de inicialização (sem `wait-for-it.sh`)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
