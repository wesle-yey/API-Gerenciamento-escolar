import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from database.base import Base
from database.database import get_db
from main import app

# Configuração do banco de teste em memória
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Criar tabelas de teste
Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

# Substituir a dependência do banco
app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

class TestAPI:
    """Testes para as funcionalidades principais da API"""
    
    def setup_method(self):
        """Setup antes de cada teste"""
        # Limpar banco antes de cada teste
        Base.metadata.drop_all(bind=engine)
        Base.metadata.create_all(bind=engine)

        # Criar usuário de teste
        self.test_user = {
            "username": "testuser",
            "password": "testpass123"
        }

        # Registrar usuário
        client.post("/register", data=self.test_user)  # precisa ser `data`

        # Login para obter token
        login_response = client.post(
            "/api/login",
            data=self.test_user,  # form-urlencoded
            headers={"Content-Type": "application/x-www-form-urlencoded"}
        )

        assert login_response.status_code == 200

        try:
            self.access_token = login_response.json().get("access_token")
        except Exception:
            self.access_token = None

        self.headers = {"Authorization": f"Bearer {self.access_token}"} if self.access_token else {}

    def test_criar_curso_e_verificar_lista(self):
        """Teste: Criar um curso e verificar se aparece na lista"""
        curso_data = {
            "nome": "Introdução à Programação",
            "descricao": "Curso básico de Python"
        }

        response = client.post("/cursos/adicionar", json=curso_data, headers=self.headers)
        assert response.status_code == 200

        response = client.get("/cursos", headers=self.headers)
        assert response.status_code == 200
        assert "Introdução à Programação" in response.text
        assert "Curso básico de Python" in response.text
    
    def test_criar_aluno_e_verificar_lista(self):
        """Teste: Criar um aluno e verificar se aparece na lista"""
        # Criar primeiro o curso (obrigatório)
        curso_data = {
            "nome": "Matemática",
            "descricao": "Curso de matemática básica"
        }
        curso_resp = client.post("/cursos/adicionar", json=curso_data, headers=self.headers)
        assert curso_resp.status_code == 200

        # Criar aluno associado ao curso id=1
        aluno_data = {
            "nome": "João Silva",
            "curso_id": 1
        }

        response = client.post("/alunos/adicionar", json=aluno_data, headers=self.headers)
        assert response.status_code == 200

        response = client.get("/alunos", headers=self.headers)
        assert response.status_code == 200
        assert "João Silva" in response.text
    
    def test_criar_professor_e_verificar_lista(self):
        """Teste: Criar um professor e verificar se aparece na lista"""
        professor_data = {
            "nome": "Dr. Carlos",
            "especializacao": "Matemática",
            "departamento": "Ciências Exatas"
        }

        response = client.post("/professores/adicionar", json=professor_data, headers=self.headers)
        assert response.status_code == 200

        response = client.get("/professores", headers=self.headers)
        assert response.status_code == 200
        assert "Dr. Carlos" in response.text
        assert "Matemática" in response.text
        assert "Ciências Exatas" in response.text
    
    def test_editar_curso(self):
        """Teste: Editar um curso existente"""
        curso_data = {
            "nome": "História",
            "descricao": "História antiga"
        }
        client.post("/cursos/adicionar", json=curso_data, headers=self.headers)

        curso_editado = {
            "nome": "História Moderna",
            "descricao": "História dos séculos XVI-XIX"
        }

        response = client.post("/cursos/editar/1", json=curso_editado, headers=self.headers)
        assert response.status_code == 200

        response = client.get("/cursos", headers=self.headers)
        assert response.status_code == 200
        assert "História Moderna" in response.text
        assert "História dos séculos XVI-XIX" in response.text
    
    def test_deletar_curso(self):
        """Teste: Deletar um curso"""
        curso_data = {
            "nome": "Geografia",
            "descricao": "Geografia física"
        }
        client.post("/cursos/adicionar", json=curso_data, headers=self.headers)

        response = client.get("/cursos", headers=self.headers)
        assert "Geografia" in response.text

        response = client.get("/cursos/remover/1", headers=self.headers)
        assert response.status_code == 200

        response = client.get("/cursos", headers=self.headers)
        assert "Geografia" not in response.text
    
    def test_autenticacao_obrigatoria(self):
        """Teste: Verificar se rotas protegidas exigem autenticação"""
        response = client.get("/cursos")
        assert response.status_code == 401
    
    def test_registro_usuario(self):
        """Teste: Registrar novo usuário"""
        novo_usuario = {
            "username": "novousuario",
            "password": "senha123"
        }

        response = client.post("/register", data=novo_usuario)  # precisa ser `data`
        assert response.status_code == 200

        login_response = client.post(
            "/api/login",
            data=novo_usuario,
            headers={"Content-Type": "application/x-www-form-urlencoded"}
        )
        assert login_response.status_code == 200
