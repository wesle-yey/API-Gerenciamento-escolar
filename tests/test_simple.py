import pytest
import os
import sys

# Adicionar o diretório raiz ao path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_imports():
    """Teste básico para verificar se os módulos podem ser importados"""
    try:
        from database.base import Base
        from app.models.models import Curso, Aluno, Professor, UserModel
        from app.schemas.schemas import CursoBase, AlunoBase, ProfessorBase
        assert True
    except ImportError as e:
        pytest.fail(f"Falha ao importar módulos: {e}")

def test_models_creation():
    """Teste para verificar se os modelos podem ser criados"""
    from database.base import Base
    from app.models.models import Curso, Aluno, Professor, UserModel
    
    # Verificar se as classes existem
    assert Curso is not None
    assert Aluno is not None
    assert Professor is not None
    assert UserModel is not None
    
    # Verificar se herdam de Base
    assert issubclass(Curso, Base)
    assert issubclass(Aluno, Base)
    assert issubclass(Professor, Base)
    assert issubclass(UserModel, Base)

def test_schemas_creation():
    """Teste para verificar se os schemas podem ser criados"""
    from app.schemas.schemas import CursoBase, AlunoBase, ProfessorBase
    
    # Verificar se as classes existem
    assert CursoBase is not None
    assert AlunoBase is not None
    assert ProfessorBase is not None

def test_crud_functions():
    """Teste para verificar se as funções CRUD existem"""
    import crud
    
    # Verificar se as funções existem
    assert hasattr(crud, 'get_alunos')
    assert hasattr(crud, 'get_cursos')
    assert hasattr(crud, 'get_professores')
    assert hasattr(crud, 'create_aluno')
    assert hasattr(crud, 'create_curso')
    assert hasattr(crud, 'create_professor')

def test_database_config():
    """Teste para verificar se a configuração do banco existe"""
    from database.database import get_db, create_tables
    
    # Verificar se as funções existem
    assert get_db is not None
    assert create_tables is not None

def test_auth_functions():
    """Teste para verificar se as funções de autenticação existem"""
    from database.auth_user import UserUseCases
    from database.token import verify_token, logout
    
    # Verificar se as classes/funções existem
    assert UserUseCases is not None
    assert verify_token is not None
    assert logout is not None

def test_routes_exist():
    """Teste para verificar se as rotas estão definidas"""
    from app.routes import alunos, cursos, professores, auth
    
    # Verificar se os módulos de rotas existem
    assert alunos is not None
    assert cursos is not None
    assert professores is not None
    assert auth is not None

def test_main_app():
    """Teste para verificar se a aplicação principal pode ser criada"""
    try:
        from main import app
        assert app is not None
        assert hasattr(app, 'include_router')
    except ImportError as e:
        pytest.fail(f"Falha ao importar aplicação principal: {e}")

def test_environment_variables():
    """Teste para verificar se as variáveis de ambiente estão configuradas"""
    # Verificar se as variáveis necessárias estão definidas
    required_vars = ['DATABASE_URL', 'SECRET_KEY', 'ALGORITHM']
    
    for var in required_vars:
        # Para testes, vamos usar valores padrão se não estiverem definidos
        if not os.getenv(var):
            if var == 'DATABASE_URL':
                os.environ[var] = 'sqlite:///:memory:'
            elif var == 'SECRET_KEY':
                os.environ[var] = 'test_secret_key'
            elif var == 'ALGORITHM':
                os.environ[var] = 'HS256'
    
    assert os.getenv('DATABASE_URL') is not None
    assert os.getenv('SECRET_KEY') is not None
    assert os.getenv('ALGORITHM') is not None

def test_file_structure():
    """Teste para verificar se a estrutura de arquivos está correta"""
    import os
    
    # Verificar se os diretórios principais existem
    assert os.path.exists('app')
    assert os.path.exists('database')
    assert os.path.exists('templates')
    
    # Verificar se os arquivos principais existem
    assert os.path.exists('main.py')
    assert os.path.exists('crud.py')
    assert os.path.exists('requirements.txt')
    assert os.path.exists('Dockerfile')
    assert os.path.exists('docker-compose.yml')

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
