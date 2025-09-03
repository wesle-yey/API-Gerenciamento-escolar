# Dockerfile simplificado para Render
FROM python:3.11-slim

# Instalar dependências do sistema básicas
RUN apt-get update && apt-get install -y --no-install-recommends \
  libpq-dev \
  curl \
  && rm -rf /var/lib/apt/lists/* \
  && apt-get clean

# Definir diretório de trabalho
WORKDIR /app

# Copiar requirements primeiro para cache
COPY requirements-minimal.txt .

# Instalar dependências Python
RUN pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir -r requirements-minimal.txt

# Copiar código da aplicação
COPY . .

# Criar usuário não-root
RUN groupadd -r appuser && useradd -r -g appuser -d /app -s /bin/bash appuser
RUN chown -R appuser:appuser /app
USER appuser

# Definir variáveis de ambiente
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Expor porta
EXPOSE 8000

# Healthcheck simples
HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
  CMD curl -f http://localhost:8000/health || exit 1

# Comando de inicialização
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]