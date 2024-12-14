# 🏫 API de Gerenciamento Escolar

Bem-vindo ao repositório da **API de Gerenciamento Escolar**, um projeto RESTful desenvolvido com **FastAPI** para gerenciar alunos, cursos e professores. Ideal para sistemas educacionais simples, esta API permite realizar operações CRUD básicas em diversas entidades do sistema.

---

## ✨ Funcionalidades

### 👨‍🎓 **Alunos**

- **Campos:**
  - `id`

  - `nome`

  - `curso\_id` (referência ao curso do aluno)

### 👨‍🔬 **Professores**

- **Campos:**
  - `id`
  - `nome`
  - `especialização`
  - `departamento`

### 📝 **Cursos**

- **Campos:**
  - `id`
  - `nome`
  - `descrição`

---

## 👨‍💻 Como Instalar e Executar o Projeto

### **Pré-requisitos**

- **Python 3.8 ou superior** instalado.
- Ferramenta de gerenciamento de pacotes como `pip`.

### **Passo a Passo**

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/wesle-yey/API-Gerenciamento-escolar.git
   ```

2. **Crie e ative um ambiente virtual:**

   ```bash
   python -m venv venv
   ```

   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **Linux/macOS:**
     ```bash
     source venv/bin/activate
     ```

3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Execute o projeto:**

   ```bash
   uvicorn main:app --reload
   ```

   O servidor será iniciado em: [http://127.0.0.1:8000](http://127.0.0.1:8000)

5. **Acesse a documentação interativa:**

   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🔄 Exemplo de Requisições

### **Rota: Cursos**

#### **POST** - Criar um novo curso:

- **URL:**
  ```
  http://127.0.0.1:8000/cursos
  ```
- **Body (JSON):**
  ```json
  {
      "nome": "Introdução à Programação",
      "descricao": "Curso básico de Python"
  }
  ```

#### **GET** - Listar todos os cursos:

- **URL:**
  ```
  http://127.0.0.1:8000/cursos
  ```

#### **PUT** - Atualizar um curso:

- **URL:**
  ```
  http://127.0.0.1:8000/cursos/{curso_id}
  ```
- **Body (JSON):**
  ```json
  {
      "nome": "Programação Avançada",
      "descricao": "Curso intermediário de Python"
  }
  ```

#### **DELETE** - Remover um curso:

- **URL:**
  ```
  http://127.0.0.1:8000/cursos/{curso_id}
  ```

### **Rotas: Alunos e Professores**

Para as rotas de **Alunos** e **Professores**, substitua `cursos` na URL pelos respectivos nomes:

- **Alunos:** `/alunos`
- **Professores:** `/professores`

Os dados enviados e recebidos seguem o mesmo formato, com campos especificados em suas entidades.

---

## 📚 Rotas Disponíveis

### **Cursos**

- `GET /cursos`: Lista todos os cursos.
- `GET /cursos/{curso_id}`: Retorna detalhes de um curso.
- `POST /cursos`: Cria um novo curso.
- `PUT /cursos/{curso_id}`: Atualiza um curso existente.
- `DELETE /cursos/{curso_id}`: Remove um curso.

### **Alunos**

- `GET /alunos`: Lista todos os alunos.
- `GET /alunos/{aluno_id}`: Retorna detalhes de um aluno.
- `POST /alunos`: Cria um novo aluno.
- `PUT /alunos/{aluno_id}`: Atualiza um aluno existente.
- `DELETE /alunos/{aluno_id}`: Remove um aluno.

### **Professores**

- `GET /professores`: Lista todos os professores.
- `GET /professores/{professor_id}`: Retorna detalhes de um professor.
- `POST /professores`: Cria um novo professor.
- `PUT /professores/{professor_id}`: Atualiza um professor existente.
- `DELETE /professores/{professor_id}`: Remove um professor.

---

## 🤝 Contribuições

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork deste repositório.
2. Crie uma nova branch:
   ```bash
   git checkout -b minha-feature
   ```
3. Commit suas alterações:
   ```bash
   git commit -m "Adiciona nova feature"
   ```
4. Envie para sua branch:
   ```bash
   git push origin minha-feature
   ```
5. Abra um Pull Request!

---

## 🛠️ Tecnologias Utilizadas

- **Python** (FastAPI, SQLAlchemy)
- **SQLite** (banco de dados padrão, mas pode ser substituído por outros SGBDs)
- **Uvicorn** (servidor ASGI)

---

Desenvolvido por Wesley.

