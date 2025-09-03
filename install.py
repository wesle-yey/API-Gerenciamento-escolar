#!/usr/bin/env python3
"""
Script de instalação simples e funcional
"""
import subprocess
import sys
import os

def run_command(cmd):
    """Executa comando e retorna resultado"""
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {cmd}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {cmd}")
        print(f"Erro: {e.stderr}")
        return False

def install_dependencies():
    """Instala dependências de forma segura"""
    print("🚀 Instalando dependências...")
    
    # Atualizar pip
    if not run_command("python -m pip install --upgrade pip"):
        print("❌ Falha ao atualizar pip")
        return False
    
    # Instalar do requirements.txt
    if not run_command("pip install -r requirements.txt"):
        print("❌ Falha ao instalar requirements.txt")
        return False
    
    print("✅ Dependências instaladas com sucesso!")
    return True

def test_imports():
    """Testa importações básicas"""
    print("\n🧪 Testando importações...")
    
    try:
        import fastapi
        print("✅ FastAPI importado")
    except ImportError as e:
        print(f"❌ FastAPI: {e}")
        return False
    
    try:
        import uvicorn
        print("✅ Uvicorn importado")
    except ImportError as e:
        print(f"❌ Uvicorn: {e}")
        return False
    
    try:
        import sqlalchemy
        print("✅ SQLAlchemy importado")
    except ImportError as e:
        print(f"❌ SQLAlchemy: {e}")
        return False
    
    return True

def test_app():
    """Testa se a aplicação pode ser importada"""
    print("\n🚀 Testando aplicação...")
    
    try:
        # Configurar variáveis de ambiente
        os.environ['DATABASE_URL'] = 'sqlite:///:memory:'
        os.environ['SECRET_KEY'] = 'test_secret_key'
        os.environ['ALGORITHM'] = 'HS256'
        os.environ['CORS_ORIGINS'] = '*'
        
        import main
        print("✅ Aplicação importada com sucesso")
        return True
    except Exception as e:
        print(f"❌ Erro ao importar aplicação: {e}")
        return False

def main():
    """Função principal"""
    print("🔧 Instalador - Sistema Gerenciamento Escolar")
    print("=" * 50)
    
    # Instalar dependências
    if not install_dependencies():
        print("❌ Falha na instalação")
        return False
    
    # Testar importações
    if not test_imports():
        print("❌ Falha nos testes de importação")
        return False
    
    # Testar aplicação
    if not test_app():
        print("❌ Falha ao testar aplicação")
        return False
    
    print("\n🎉 Instalação concluída com sucesso!")
    print("Agora você pode executar: uvicorn main:app --host 0.0.0.0 --port 8000")
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
