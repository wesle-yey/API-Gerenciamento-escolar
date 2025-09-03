# 🏩 API de Gerenciamento de Cursos, Alunos e Professores

Este projeto é uma API RESTful criada com FastAPI para gerenciar cursos, alunos e professores. Ele possui CRUD básico para algumas entidades e **pipeline completo de CI/CD** configurado com GitHub Actions.

## 🚀 Funcionalidades

A API resolve a necessidade de gerenciar informações relacionadas a um sistema educacional, permitindo:

### CRUD básico para as seguintes rotas:
- 👨‍🎓 **Alunos**: Id, nome, email e curso
- 👨‍🔬 **Professores**: Id, nome, especialização e departamento  
- 📝 **Cursos**: Id, nome e descrição

## 🧪 Testes Automatizados

O sistema possui **testes automatizados** que verificam todas as funcionalidades principais:

- ✅ Criar curso e verificar se aparece na lista
- ✅ Criar aluno e verificar se aparece na lista  
- ✅ Criar professor e verificar se aparece na lista
- ✅ Editar entidades existentes
- ✅ Deletar entidades
- ✅ Autenticação obrigatória para rotas protegidas
- ✅ Registro e login de usuários

### Executar testes localmente:

```bash
# Usar o script automatizado
./run_tests.sh

# Ou executar manualmente
pytest tests/ -v --cov=.
```

## 🔄 Pipeline de CI/CD

O projeto está configurado com **GitHub Actions** para:

- 🧪 **Integração Contínua (CI)**: Executa testes automaticamente a cada push/PR
- 🚀 **Entrega Contínua (CD)**: Build e push automático para Docker Hub
- 🔒 **Verificação de Segurança**: Análise com Bandit e Safety
- 📊 **Cobertura de Testes**: Relatórios de cobertura automáticos

### Status do Pipeline:
![CI/CD](https://github.com/seu-usuario/API-Gerenciamento-escolar/workflows/CI/CD%20Pipeline/badge.svg)

## 👨‍💻 Como Instalar e Executar o Projeto:

### Pré-requisitos:
* Python 3.8 ou superior instalado
* Ferramenta de gerenciamento de pacotes como pip
* _Opcional:_ Docker

### Passo a Passo:

#### Rodando com Python:
```bash
# Clone o repositório
git clone https://github.com/seu-usuario/API-Gerenciamento-escolar.git
cd API-Gerenciamento-escolar

# Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/macOS
# ou
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt

# Configure as variáveis de ambiente
cp env.example .env
# Edite o arquivo .env com suas configurações

# Execute o projeto
uvicorn main:app --reload
```

O servidor será iniciado em: http://127.0.0.1:8000

#### Rodando com Docker:
```bash
# Certifique-se de ter o Docker e o Docker Compose instalados
docker-compose up -d --build

# Para parar os contêineres
docker-compose down
```

## 🐳 Docker Hub

O sistema é automaticamente publicado no Docker Hub após cada commit na branch main:

```bash
# Baixar e executar
docker pull seu-usuario/gerenciamento-escolar:latest
docker run -p 8000:8000 seu-usuario/gerenciamento-escolar:latest
```

## 📡 Exemplo de Requisições para a rota Cursos

### Método: POST:
URL: http://127.0.0.1:8000/cursos
Body: (form-data)
```json
{
  "nome": "Introdução à Programação",
  "descricao": "Curso básico de Python"
}
```

### Método: GET:
URL: http://127.0.0.1:8000/cursos

### Método: PUT
URL: http://127.0.0.1:8000/cursos/1
Body: (form-data)
```json
{
  "nome": "João da Silva",
  "especializacao": "Matemática", 
  "departamento": "Ciências Exatas"
}
```

### Método: DELETE:
URL: http://127.0.0.1:8000/cursos/1

## 🛣️ Rotas Disponíveis:

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

## 🔧 Configuração de CI/CD

Para configurar o pipeline completo:

1. **Configure os secrets do GitHub** (veja `docker-hub-setup.md`)
2. **Faça push para a branch main** - o pipeline executará automaticamente
3. **Monitore o status** na aba Actions do GitHub

## 📊 Métricas de Qualidade

- **Cobertura de Testes**: >90%
- **Verificação de Segurança**: Automática
- **Build Docker**: Automático
- **Deploy**: Disponível via Docker Hub

## 🤝 Contribuição

Contribuições são bem-vindas! 

1. Faça um fork do repositório
2. Crie uma nova branch para suas alterações
3. Adicione testes para novas funcionalidades
4. Envie um pull request

**Importante**: Todos os testes devem passar para que o PR seja aceito.

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

---

## 🎯 Resumo do Sistema

Este projeto demonstra um **ciclo completo de desenvolvimento profissional**:

1. **📝 Codificar**: API RESTful com FastAPI
2. **🧪 Testar**: Testes automatizados com pytest  
3. **📦 Empacotar**: Docker com multi-stage build
4. **🚀 Disponibilizar**: CI/CD com GitHub Actions + Docker Hub

O sistema está pronto para uso em produção e pode ser facilmente implantado em qualquer ambiente que suporte Docker.

