from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine
import models
from routers import aluno, curso, professor

# Criação das tabelas no banco
models.Base.metadata.create_all(bind=engine)

# Configuração da aplicação
app = FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclusão das rotas
app.include_router(aluno.router, prefix="/alunos", tags=["Alunos"])
app.include_router(curso.router, prefix="/cursos", tags=["Cursos"])
app.include_router(professor.router, prefix="/professores", tags=["Professores"])


@app.get("/")
def root():
    return {"message": "API de Gerenciamento Escolar funcionando! Use as rotas Aluno, Professor e Curso!"}
