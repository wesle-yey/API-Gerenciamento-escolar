#!/usr/bin/env python3
"""
Script de teste simples para verificar se tudo está funcionando
"""
import os
import sys
import subprocess

def test_imports():
    """Testa se as importações básicas funcionam"""
    print("🧪 Testando importações básicas...")
    
    try:
        import fastapi
        print("✅ FastAPI importado com sucesso")
    except ImportError as e:
        print(f"❌ Erro ao importar FastAPI: {e}")
        return False
    
    try:
        import uvicorn
        print("✅ Uvicorn importado com sucesso")
    except ImportError as e:
        print(f"❌ Erro ao importar Uvicorn: {e}")
        return False
    
    try:
        import sqlalchemy
        print("✅ SQLAlchemy importado com sucesso")
    except ImportError as e:
        print(f"❌ Erro ao importar SQLAlchemy: {e}")
        return False
    
    return True

def test_main_file():
    """Testa se o arquivo main.py pode ser importado"""
    print("\n🧪 Testando arquivo main.py...")
    
    try:
        # Configurar variáveis de ambiente para teste
        os.environ['DATABASE_URL'] = 'sqlite:///:memory:'
        os.environ['SECRET_KEY'] = 'test_secret_key'
        os.environ['ALGORITHM'] = 'HS256'
        os.environ['CORS_ORIGINS'] = '*'
        
        # Tentar importar o main
        import main
        print("✅ Arquivo main.py importado com sucesso")
        return True
    except Exception as e:
        print(f"❌ Erro ao importar main.py: {e}")
        return False

def test_basic_math():
    """Testa operações básicas"""
    print("\n🧪 Testando operações básicas...")
    
    try:
        assert 2 + 2 == 4
        assert 10 * 5 == 50
        assert 100 / 10 == 10
        print("✅ Operações matemáticas básicas funcionando")
        return True
    except Exception as e:
        print(f"❌ Erro nas operações matemáticas: {e}")
        return False

def run_pytest():
    """Executa os testes com pytest"""
    print("\n🧪 Executando testes com pytest...")
    
    try:
        result = subprocess.run([
            sys.executable, "-m", "pytest", 
            "tests/test_basic.py", "-v"
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Todos os testes passaram!")
            print(result.stdout)
            return True
        else:
            print("❌ Alguns testes falharam!")
            print(result.stdout)
            print(result.stderr)
            return False
    except Exception as e:
        print(f"❌ Erro ao executar pytest: {e}")
        return False

def main():
    """Função principal"""
    print("🚀 Sistema de Gerenciamento Escolar - Teste Local")
    print("=" * 50)
    
    tests = [
        test_imports,
        test_main_file,
        test_basic_math,
        run_pytest
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 50)
    print(f"📊 Resultado: {passed}/{total} testes passaram")
    
    if passed == total:
        print("🎉 Todos os testes passaram! Aplicação pronta para deploy.")
        return True
    else:
        print("💥 Alguns testes falharam. Verifique os erros acima.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
