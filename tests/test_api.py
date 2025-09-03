import pytest
from fastapi.testclient import TestClient
from main import app
from app.models.models import UserModel
from database.database import get_db, Base, engine
from sqlalchemy.orm import Session

# ===================== SETUP DO TESTE =====================
# Cria a tabela de teste
Base.metadata.create_all(bind=engine)
client = TestClient(app)

TEST_USER = {"username": "testuser", "password": "123456"}

def get_access_token(client: TestClient, username: str, password: str):
    """Função auxiliar para registrar usuário e obter token de acesso."""
    # Registrar usuário
    client.post("/register", data={"username": username, "password": password})
    # Fazer login
    response = client.post("/api/login", data={"username": username, "password": password})
    assert response.status_code == 200
    access_token = response.json()["access_token"]
    return access_token

# ===================== TESTES =====================
class TestAPI:
    @pytest.fixture(autouse=True)
    def setup(self):
        # Obter token e headers para rotas autenticadas
        token = get_access_token(client, TEST_USER["username"], TEST_USER["password"])
        self.auth_headers = {"Authorization": f"Bearer {token}"}

    def test_homepage(self):
        response = client.get("/", headers=self.auth_headers)
        assert response.status_code == 200
        assert "text/html" in response.headers["content-type"]

    def test_criar_curso_e_verificar_lista(self):
        curso_data = {"nome": "Matemática", "descricao": "Curso de matemática básica"}
        response = client.post("/cursos/adicionar", data=curso_data, headers=self.auth_headers)
        assert response.status_code == 303  # Redirect response

        response = client.get("/cursos", headers=self.auth_headers)
        assert response.status_code == 200
        assert "Matemática" in response.text

    def test_criar_aluno_associado_a_curso(self):
        # Criar curso
        curso_data = {"nome": "Física", "descricao": "Curso de física básica"}
        client.post("/cursos/adicionar", data=curso_data, headers=self.auth_headers)

        aluno_data = {"nome": "João", "curso_id": 1}
        response = client.post("/alunos/adicionar", data=aluno_data, headers=self.auth_headers)
        assert response.status_code == 303  # Redirect response

    def test_criar_professor_e_verificar_lista(self):
        professor_data = {"nome": "Prof. Silva", "especializacao": "Matemática", "departamento": "Ciências"}
        response = client.post("/professores/adicionar", data=professor_data, headers=self.auth_headers)
        assert response.status_code == 303  # Redirect response

        response = client.get("/professores", headers=self.auth_headers)
        assert response.status_code == 200
        assert "Prof. Silva" in response.text

    def test_editar_curso(self):
        # Criar curso
        curso_data = {"nome": "História", "descricao": "História antiga"}
        client.post("/cursos/adicionar", data=curso_data, headers=self.auth_headers)

        # Editar curso usando a rota POST que existe
        updated_data = {"nome": "História Moderna", "descricao": "História dos séculos XVI-XIX"}
        response = client.post("/cursos/editar/1", data=updated_data, headers=self.auth_headers)
        assert response.status_code == 303  # Redirect response

    def test_deletar_curso(self):
        curso_data = {"nome": "Química", "descricao": "Química básica"}
        client.post("/cursos/adicionar", data=curso_data, headers=self.auth_headers)

        # Usar a rota GET que existe para remover
        response = client.get("/cursos/remover/1", headers=self.auth_headers)
        assert response.status_code == 303  # Redirect response

    def test_autenticacao_obrigatoria(self):
        # Teste sem token
        response = client.get("/cursos")
        assert response.status_code == 401

    def test_registro_usuario_e_login(self):
        username = "novo_user"
        password = "123456"
        # Registrar usuário
        response = client.post("/register", data={"username": username, "password": password})
        assert response.status_code == 303 or response.status_code == 200

        # Login
        response = client.post("/api/login", data={"username": username, "password": password})
        assert response.status_code == 200
        assert "access_token" in response.json()
