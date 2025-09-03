# Multi-stage build para otimização
FROM python:3.11-slim as builder

# Instalar dependências do sistema com versões fixas para segurança
RUN apt-get update && apt-get install -y --no-install-recommends \
  gcc=4:11.2.0-1ubuntu1 \
  g++=4:11.2.0-1ubuntu1 \
  libpq-dev=14.9-0ubuntu0.22.04.1 \
  && rm -rf /var/lib/apt/lists/* \
  && apt-get clean

WORKDIR /app

# Copiar e instalar dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt

# Stage de produção
FROM python:3.11-slim

# Instalar dependências do sistema necessárias para runtime com versões fixas
RUN apt-get update && apt-get install -y --no-install-recommends \
  libpq5=14.9-0ubuntu0.22.04.1 \
  curl=7.81.0-1ubuntu1.10 \
  && rm -rf /var/lib/apt/lists/* \
  && apt-get clean

# Criar usuário não-root para segurança
RUN groupadd -r appuser && useradd -r -g appuser -d /app -s /bin/bash appuser

WORKDIR /app

# Copiar dependências Python instaladas
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copiar código da aplicação
COPY --chown=appuser:appuser . .

# Definir variáveis de ambiente
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PATH="/usr/local/bin:$PATH"
ENV PYTHONIOENCODING=utf-8

# Mudar para usuário não-root
USER appuser

# Expor porta
EXPOSE 8000

# Healthcheck melhorado
HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
  CMD curl -f http://localhost:8000/health || exit 1

# Comando de inicialização com configurações otimizadas
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "1", "--access-log"]
