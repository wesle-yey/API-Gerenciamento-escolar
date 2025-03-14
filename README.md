# 🏩 API de Gerenciamento de Cursos, Alunos e Professores
Este projeto é uma API RESTful criada com FastAPI para gerenciar cursos, alunos e professores. Ele possui CRUD básico para algumas entidades. A API é ideal para sistemas educacionais simples que precisam de funcionalidades básicas para manipular dados.

A API resolve a necessidade de gerenciar informações relacionadas a um sistema educacional, permitindo:

## CRUD básico para as seguintes rotas:
### 👨‍🎓 Alunos:
Id, nome, email e curso

### 👨‍🔬 Professores:
Id, nome, especialização e departamento

### 📝 Cursos:
Id, nome e descrição

## 👨‍💻 Como Instalar e Executar o Projeto:
### Pré-requisitos:
* Python 3.8 ou superior instalado.
* Ferramenta de gerenciamento de pacotes como pip.
* _Opcional:_ Docker

### Passo a Passo:
#### Rodando com Python:
* Clone o repositório:
```
git clone https://github.com/wesle-yey/API-Gerenciamento-escolar.git
```

* Crie e ative um ambiente virtual
```
python -m venv venv
```
# No Windows:
```
venv\Scripts\activate
```
# No Linux/macOS:
```
source venv/bin/activate
```

* Instale as dependências
```
pip install -r requirements.txt
```

* Execute o projeto:
```
uvicorn main:app --reload
```
O servidor será iniciado em: http://127.0.0.1:8000.

#### Rodando com Docker:
Se preferir rodar o projeto usando Docker, basta executar os seguintes comandos:

* Certifique-se de ter o Docker e o Docker Compose instalados.
* No terminal, dentro da pasta do projeto, execute:
```
docker-compose up -d --build
```
Isso irá construir e iniciar os contêineres em segundo plano.

Para parar os contêineres, use:
```
docker-compose down
```

# Exemplo de Requisições para a rota Cursos

## Método: POST:
URL: http://127.0.0.1:8000/cursos,
Body: (form-data)
```
{
"nome": "Introdução à Programação",
"descricao": "Curso básico de Python"
}
```

## Método: GET:
URL: http://127.0.0.1:8000/cursos

## Método: PUT
URL: http://127.0.0.1:8000/cursos/1,
Body: (form-data)
```
{
"nome": "João da Silva",
"especializacao": "Matemática",
"departamento": "Ciências Exatas"
}
```

## Método: DELETE:
URL: http://127.0.0.1:8000/cursos/1

### Para as outras rotas, basta substituir "cursos" na URL por "alunos" ou "professores", mas aqui está um guia geral de todas as rotas disponíveis:
# Rotas Disponíveis:
### Cursos	
* GET /cursos - Lista todos os cursos
* GET /cursos/{curso_id} - Retorna curso pelo ID
* POST /cursos - Cria um novo curso
* PUT /cursos/{curso_id} - Atualiza um curso pelo ID
* DELETE /cursos/{curso_id} - Remove um curso pelo ID

### Alunos
* GET /alunos - Lista todos os alunos
* GET /alunos/{aluno_id} - Retorna aluno pelo ID
* POST /alunos - Cria um novo aluno
* PUT /alunos/{aluno_id} - Atualiza um aluno pelo ID
* DELETE /alunos/{aluno_id} - Remove um aluno pelo ID

### Professores
* GET /professores - Lista todos os professores
* GET /professores/{professor_id} - Retorna professor pelo ID
* POST /professores - Cria um novo professor
* PUT /professores/{professor_id} - Atualiza um professor pelo ID
* DELETE /professores/{professor_id} - Remove um professor pelo ID

### Contribuição
Contribuições são bem-vindas! Faça um fork do repositório, crie uma nova branch para suas alterações e envie um pull request.

