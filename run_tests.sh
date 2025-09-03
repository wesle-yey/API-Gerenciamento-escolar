#!/bin/bash

echo "🧪 Executando testes do Sistema de Gerenciamento Escolar..."
echo "=================================================="

# Verificar se Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 não encontrado. Instale Python 3.9+ primeiro."
    exit 1
fi

# Verificar se pip está instalado
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 não encontrado. Instale pip primeiro."
    exit 1
fi

echo "✅ Python e pip encontrados"

# Criar ambiente virtual se não existir
if [ ! -d "venv" ]; then
    echo "📦 Criando ambiente virtual..."
    python3 -m venv venv
fi

# Ativar ambiente virtual
echo "🔧 Ativando ambiente virtual..."
source venv/bin/activate

# Instalar dependências
echo "📚 Instalando dependências..."
pip install -r requirements.txt

# Instalar dependências de teste
echo "🧪 Instalando dependências de teste..."
pip install pytest pytest-cov

# Configurar variáveis de ambiente para teste
echo "🔧 Configurando ambiente de teste..."
export DATABASE_URL="sqlite:///:memory:"
export SECRET_KEY="test_secret_key_for_testing_purposes_only"
export ALGORITHM="HS256"

# Executar testes
echo "🚀 Executando testes..."
pytest tests/ -v --tb=short --cov=. --cov-report=term-missing

# Verificar resultado dos testes
if [ $? -eq 0 ]; then
    echo "✅ Todos os testes passaram!"
    echo "🎉 Sistema está funcionando corretamente!"
else
    echo "❌ Alguns testes falharam!"
    echo "🔍 Verifique os logs acima para mais detalhes."
    exit 1
fi

echo "=================================================="
echo "🏁 Execução dos testes concluída!"
