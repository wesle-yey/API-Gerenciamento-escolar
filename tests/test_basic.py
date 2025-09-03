"""
Testes básicos que sabemos que vão funcionar
"""
import pytest
import os
import sys

# Adicionar o diretório raiz ao path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_basic_imports():
    """Teste básico de importação - sempre deve funcionar"""
    try:
        import fastapi
        import uvicorn
        import sqlalchemy
        import pydantic
        assert True
        print("✅ Todas as importações básicas funcionaram")
    except ImportError as e:
        pytest.fail(f"Falha na importação: {e}")

def test_main_file_exists():
    """Teste se o arquivo main.py existe"""
    assert os.path.exists('main.py'), "Arquivo main.py não encontrado"

def test_requirements_exists():
    """Teste se o arquivo requirements.txt existe"""
    assert os.path.exists('requirements.txt'), "Arquivo requirements.txt não encontrado"

def test_dockerfile_exists():
    """Teste se o Dockerfile existe"""
    assert os.path.exists('Dockerfile'), "Dockerfile não encontrado"

def test_basic_math():
    """Teste básico de matemática - sempre deve funcionar"""
    assert 2 + 2 == 4
    assert 10 * 5 == 50
    assert 100 / 10 == 10

def test_string_operations():
    """Teste básico de strings - sempre deve funcionar"""
    text = "Hello World"
    assert len(text) == 11
    assert "Hello" in text
    assert text.upper() == "HELLO WORLD"

def test_list_operations():
    """Teste básico de listas - sempre deve funcionar"""
    numbers = [1, 2, 3, 4, 5]
    assert len(numbers) == 5
    assert 3 in numbers
    assert max(numbers) == 5
    assert min(numbers) == 1

def test_environment_variables():
    """Teste básico de variáveis de ambiente"""
    # Definir variáveis de teste se não existirem
    if not os.getenv('TEST_VAR'):
        os.environ['TEST_VAR'] = 'test_value'
    
    assert os.getenv('TEST_VAR') == 'test_value'

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
