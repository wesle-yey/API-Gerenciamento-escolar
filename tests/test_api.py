import pytest
from fastapi.testclient import TestClient
from main import app

class TestAPI:
    def setup_method(self):
        # Inicializa o client
        self.client = TestClient(app)
        self.headers = {"Content-Type": "application/x-www-form-urlencoded"}

        # Cria usuário de teste e faz login
        register_data = {"username": "teste", "password": "123456"}
        self.client.post("/register", data=register_data, headers=self.headers)

        login_response = self.client.post("/login", data=register_data, headers=self.headers)
        assert login_response.status_code == 200

        # Pega cookie de autenticação
        self.auth_headers = {"Cookie": login_response.headers.get("set-cookie")}

    def test_homepage(self):
        """Teste: A página inicial deve carregar com login"""
        response = self.client.get("/", headers=self.auth_headers)
        assert response.status_code == 200
        assert "Bem-vindo" in response.text or "Home" in response.text

    def test_criar_curso_e_verificar_lista(self):
        """Teste: Criar um curso e verificar se aparece na lista"""
        curso_data = {
            "nome": "Introdução à Programação",
            "descricao": "Curso básico de Python"
        }

        response = self.client.post("/cursos/adicionar", data=curso_data, headers=self.auth_headers)
        assert response.status_code == 200

        response = self.client.get("/cursos", headers=self.auth_headers)
        assert response.status_code == 200
        assert "Introdução à Programação" in response.text
        assert "Curso básico de Python" in response.text

    def test_criar_aluno_associado_a_curso(self):
        """Teste: Criar um aluno vinculado a um curso existente"""
        # Primeiro cria curso
        curso_data = {"nome": "Matemática", "descricao": "Curso de Matemática Básica"}
        self.client.post("/cursos/adicionar", data=curso_data, headers=self.auth_headers)

        aluno_data = {"nome": "João Silva", "curso_id": 1}
        response = self.client.post("/alunos/adicionar", data=aluno_data, headers=self.auth_headers)
        assert response.status_code == 200

        response = self.client.get("/alunos", headers=self.auth_headers)
        assert response.status_code == 200
        assert "João Silva" in response.text

    def test_criar_professor_e_verificar_lista(self):
        """Teste: Criar um professor e verificar se aparece na lista"""
        professor_data = {
            "nome": "Maria Souza",
            "especializacao": "História",
            "departamento": "Humanas"
        }
        response = self.client.post("/professores/adicionar", data=professor_data, headers=self.auth_headers)
        assert response.status_code == 200

        response = self.client.get("/professores", headers=self.auth_headers)
        assert response.status_code == 200
        assert "Maria Souza" in response.text

    def test_editar_curso(self):
        """Teste: Editar um curso existente"""
        curso_data = {"nome": "Geografia", "descricao": "Curso Geografia"}
        self.client.post("/cursos/adicionar", data=curso_data, headers=self.auth_headers)

        edit_data = {"nome": "Geografia Avançada", "descricao": "Curso Geografia Atualizado"}
        response = self.client.post("/cursos/editar/1", data=edit_data, headers=self.auth_headers)
        assert response.status_code == 200

        response = self.client.get("/cursos", headers=self.auth_headers)
        assert "Geografia Avançada" in response.text

    def test_deletar_curso(self):
        """Teste: Deletar um curso"""
        curso_data = {"nome": "História", "descricao": "Curso História"}
        self.client.post("/cursos/adicionar", data=curso_data, headers=self.auth_headers)

        response = self.client.post("/cursos/deletar/1", headers=self.auth_headers)
        assert response.status_code == 200

        response = self.client.get("/cursos", headers=self.auth_headers)
        assert "História" not in response.text

    def test_autenticacao_obrigatoria(self):
        """Teste: Verificar se rotas protegidas exigem autenticação"""
        response = self.client.get("/cursos")
        # Pode ser redirect ou não autorizado
        assert response.status_code in [401, 302, 307]

    def test_registro_usuario_e_login(self):
        """Teste: Registro de novo usuário e login"""
        # Registro
        register_data = {"username": "novo_usuario", "password": "123456"}
        response = self.client.post("/register", data=register_data, headers=self.headers)
        assert response.status_code == 200

        # Login
        login_response = self.client.post("/login", data=register_data, headers=self.headers)
        assert login_response.status_code == 200
        assert "set-cookie" in login_response.headers or "Set-Cookie" in login_response.headers
