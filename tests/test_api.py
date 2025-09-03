import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestAPI:
    def setup_method(self):
        """Setup antes de cada teste"""
        # Cabeçalho padrão para envio via formulário
        self.headers = {"Content-Type": "application/x-www-form-urlencoded"}

    def test_homepage(self):
        """Teste: Página inicial deve carregar"""
        response = client.get("/")
        assert response.status_code == 200
        assert "Bem-vindo" in response.text

    def test_criar_curso_e_verificar_lista(self):
        """Teste: Criar um curso e verificar se aparece na lista"""
        curso_data = {
            "nome": "Introdução à Programação",
            "descricao": "Curso básico de Python"
        }

        response = client.post("/cursos/adicionar", data=curso_data, headers=self.headers)
        assert response.status_code == 200

        # Verificar se o curso aparece na lista
        response = client.get("/cursos", headers=self.headers)
        assert response.status_code == 200
        assert "Introdução à Programação" in response.text
        assert "Curso básico de Python" in response.text

    def test_criar_aluno_associado_a_curso(self):
        """Teste: Criar um aluno vinculado a um curso existente"""
        # Criar curso primeiro
        curso_data = {"nome": "Matemática", "descricao": "Curso de Matemática Básica"}
        client.post("/cursos/adicionar", data=curso_data, headers=self.headers)

        # Criar aluno vinculado ao curso
        aluno_data = {"nome": "João Silva", "curso_id": 1}
        response = client.post("/alunos/adicionar", data=aluno_data, headers=self.headers)
        assert response.status_code == 200

        # Verificar se aluno aparece na lista
        response = client.get("/alunos", headers=self.headers)
        assert response.status_code == 200
        assert "João Silva" in response.text

    def test_criar_professor_e_verificar_lista(self):
        """Teste: Criar um professor e verificar se aparece na lista"""
        professor_data = {
            "nome": "Maria Souza",
            "especializacao": "História",
            "departamento": "Humanas"
        }
        response = client.post("/professores/adicionar", data=professor_data, headers=self.headers)
        assert response.status_code == 200

        # Verificar se professor aparece na lista
        response = client.get("/professores", headers=self.headers)
        assert response.status_code == 200
        assert "Maria Souza" in response.text
        assert "História" in response.text
        assert "Humanas" in response.text

    def test_editar_curso(self):
        """Teste: Editar um curso existente"""
        # Criar curso
        curso_data = {"nome": "História", "descricao": "História antiga"}
        client.post("/cursos/adicionar", data=curso_data, headers=self.headers)

        # Editar curso
        curso_editado = {"nome": "História Moderna", "descricao": "História dos séculos XVI-XIX"}
        response = client.post("/cursos/editar/1", data=curso_editado, headers=self.headers)
        assert response.status_code == 200

        # Verificar se edição foi aplicada
        response = client.get("/cursos", headers=self.headers)
        assert "História Moderna" in response.text
        assert "História dos séculos XVI-XIX" in response.text

    def test_deletar_curso(self):
        """Teste: Deletar um curso"""
        # Criar curso
        curso_data = {"nome": "Geografia", "descricao": "Geografia física"}
        client.post("/cursos/adicionar", data=curso_data, headers=self.headers)

        # Confirmar criação
        response = client.get("/cursos", headers=self.headers)
        assert "Geografia" in response.text

        # Deletar curso
        response = client.get("/cursos/remover/1", headers=self.headers)
        assert response.status_code == 200

        # Confirmar deleção
        response = client.get("/cursos", headers=self.headers)
        assert "Geografia" not in response.text

    def test_autenticacao_obrigatoria(self):
        """Teste: Verificar se rotas protegidas exigem autenticação"""
        response = client.get("/cursos", allow_redirects=False)
        # Pode ser 401 (não autorizado) ou 302 (redirecionamento para login)
        assert response.status_code in [401, 302]
        if response.status_code == 302:
            assert "/login" in response.headers["location"]

    def test_registro_usuario_e_login(self):
        """Teste: Registrar usuário e fazer login"""
        novo_usuario = {"username": "usuario1", "password": "senha123"}

        # Registro
        response = client.post("/register", data=novo_usuario, headers=self.headers)
        assert response.status_code == 200

        # Login
        response = client.post("/login", data=novo_usuario, headers=self.headers)
        assert response.status_code == 200
        assert "Set-Cookie" in response.headers  # cookie da sessão presente
