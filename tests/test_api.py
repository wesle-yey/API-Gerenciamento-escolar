import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from database.base import Base
from database.database import get_db
from main import app
import os

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
        client.post("/register", json=self.test_user)

        # Fazer login para obter token
        # Fazer login para obter token
login_response = client.post(
    "/login",
    data={"username": "testuser", "password": "testpass123"},
    headers={"Content-Type": "application/x-www-form-urlencoded"}
)
assert login_response.status_code == 200


        # Obter token do corpo da resposta (ajuste conforme retorno do backend)
        try:
            self.access_token = login_response.json().get("access_token")
        except Exception:
            self.access_token = None

        # Configurar headers para autenticação
        self.headers = {"Authorization": f"Bearer {self.access_token}"} if self.access_token else {}
    
    def test_criar_curso_e_verificar_lista(self):
        """Teste: Criar um curso e verificar se aparece na lista"""
        # Criar curso
        curso_data = {
            "nome": "Introdução à Programação",
            "descricao": "Curso básico de Python"
        }

        response = client.post("/cursos/adicionar", json=curso_data, headers=self.headers)
        assert response.status_code == 200

        # Verificar se o curso aparece na lista
        response = client.get("/cursos", headers=self.headers)
        assert response.status_code == 200
        assert "Introdução à Programação" in response.text
        assert "Curso básico de Python" in response.text
    
    def test_criar_aluno_e_verificar_lista(self):
        """Teste: Criar um aluno e verificar se aparece na lista"""
        # Primeiro criar um curso
        curso_data = {
            "nome": "Matemática",
            "descricao": "Curso de matemática básica"
        }
        client.post("/cursos/adicionar", json=curso_data, headers=self.headers)

        # Criar aluno
        aluno_data = {
            "nome": "João Silva",
            "curso_id": "1"
        }

        response = client.post("/alunos/adicionar", json=aluno_data, headers=self.headers)
        assert response.status_code == 200

        # Verificar se o aluno aparece na lista
        response = client.get("/alunos", headers=self.headers)
        assert response.status_code == 200
        assert "João Silva" in response.text
    
    def test_criar_professor_e_verificar_lista(self):
        """Teste: Criar um professor e verificar se aparece na lista"""
        # Criar professor
        professor_data = {
            "nome": "Dr. Carlos",
            "especializacao": "Matemática",
            "departamento": "Ciências Exatas"
        }

        response = client.post("/professores/adicionar", json=professor_data, headers=self.headers)
        assert response.status_code == 200

        # Verificar se o professor aparece na lista
        response = client.get("/professores", headers=self.headers)
        assert response.status_code == 200
        assert "Dr. Carlos" in response.text
        assert "Matemática" in response.text
        assert "Ciências Exatas" in response.text
    
    def test_editar_curso(self):
        """Teste: Editar um curso existente"""
        # Criar curso
        curso_data = {
            "nome": "História",
            "descricao": "História antiga"
        }
        client.post("/cursos/adicionar", json=curso_data, headers=self.headers)

        # Editar curso
        curso_editado = {
            "nome": "História Moderna",
            "descricao": "História dos séculos XVI-XIX"
        }

        response = client.post("/cursos/editar/1", json=curso_editado, headers=self.headers)
        assert response.status_code == 200

        # Verificar se foi editado
        response = client.get("/cursos", headers=self.headers)
        assert response.status_code == 200
        assert "História Moderna" in response.text
        assert "História dos séculos XVI-XIX" in response.text
    
    def test_deletar_curso(self):
        """Teste: Deletar um curso"""
        # Criar curso
        curso_data = {
            "nome": "Geografia",
            "descricao": "Geografia física"
        }
        client.post("/cursos/adicionar", json=curso_data, headers=self.headers)

        # Verificar se foi criado
        response = client.get("/cursos", headers=self.headers)
        assert "Geografia" in response.text

        # Deletar curso
        response = client.get("/cursos/remover/1", headers=self.headers)
        assert response.status_code == 200

        # Verificar se foi deletado
        response = client.get("/cursos", headers=self.headers)
        assert "Geografia" not in response.text
    
    def test_autenticacao_obrigatoria(self):
        """Teste: Verificar se rotas protegidas exigem autenticação"""
        # Tentar acessar rota protegida sem token
        response = client.get("/cursos")
        assert response.status_code == 401
    
    def test_registro_usuario(self):
        """Teste: Registrar novo usuário"""
        novo_usuario = {
            "username": "novousuario",
            "password": "senha123"
        }

        response = client.post("/register", json=novo_usuario)
        assert response.status_code == 200

        # Tentar fazer login com o novo usuário
        login_response = client.post("/login", json=novo_usuario)
        assert login_response.status_code == 200
