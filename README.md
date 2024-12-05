# API de Gerenciamento de Cursos, Alunos e Professores
Este projeto é uma API RESTful criada com FastAPI para gerenciar cursos, alunos e professores. Ele permite criar, atualizar, listar e excluir registros dessas entidades. A API é ideal para sistemas educacionais simples que precisam de funcionalidades básicas para manipular dados.

Problema que o Projeto Resolve
A API resolve a necessidade de gerenciar informações relacionadas a um sistema educacional, permitindo:

Cadastrar, atualizar, listar e excluir cursos.
Gerenciar os alunos, associando-os a cursos específicos.
Controlar os professores, incluindo especializações e departamentos.
Como Instalar e Executar o Projeto
Pré-requisitos
Python 3.8 ou superior instalado.
Ferramenta de gerenciamento de pacotes como pip.
Passo a Passo
Clone o repositório

bash
Copiar código
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
Crie e ative um ambiente virtual

bash
Copiar código
python -m venv venv
# No Windows:
venv\Scripts\activate
# No Linux/macOS:
source venv/bin/activate
Instale as dependências

bash
Copiar código
pip install fastapi uvicorn
Execute o projeto

bash
Copiar código
uvicorn main:app --reload
O servidor será iniciado em: http://127.0.0.1:8000.

Testando as Rotas Usando o Postman
Importe a coleção no Postman

Crie uma nova coleção no Postman para gerenciar as requisições.
Configure os endpoints com base nas rotas da API (ex.: GET /cursos, POST /alunos).
Exemplo de Requisição para Criar um Curso

Método: POST
URL: http://127.0.0.1:8000/cursos
Body: (form-data)
Key	Value
nome	Introdução à Programação
descricao	Curso básico de Python
Exemplo de Requisição para Listar Alunos

Método: GET
URL: http://127.0.0.1:8000/alunos
Exemplo de Requisição para Atualizar um Professor

Método: PUT
URL: http://127.0.0.1:8000/professores/1
Body: (form-data)
Key	Value
nome	João da Silva
especializacao	Matemática
departamento	Ciências Exatas
Exemplo de Requisição para Deletar um Curso

Método: DELETE
URL: http://127.0.0.1:8000/cursos/1
Rotas Disponíveis
Entidade	Método	Rota	Descrição
Cursos	GET	/cursos	Lista todos os cursos
GET	/cursos/{curso_id}	Retorna curso pelo ID
POST	/cursos	Cria um novo curso
PUT	/cursos/{curso_id}	Atualiza um curso pelo ID
DELETE	/cursos/{curso_id}	Remove um curso pelo ID
Alunos	GET	/alunos	Lista todos os alunos
GET	/alunos/{aluno_id}	Retorna aluno pelo ID
POST	/alunos	Cria um novo aluno
PUT	/alunos/{aluno_id}	Atualiza um aluno pelo ID
DELETE	/alunos/{aluno_id}	Remove um aluno pelo ID
Professores	GET	/professores	Lista todos os professores
GET	/professores/{professor_id}	Retorna professor pelo ID
POST	/professores	Cria um novo professor
PUT	/professores/{professor_id}	Atualiza um professor pelo ID
DELETE	/professores/{professor_id}	Remove um professor pelo ID
Contribuição
Contribuições são bem-vindas! Faça um fork do repositório, crie uma nova branch para suas alterações e envie um pull request.
