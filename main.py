from fastapi import FastAPI, Depends, HTTPException, Request, Form, status
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse, RedirectResponse
from sqlalchemy.orm import Session
import app.schemas.schemas as schemas, crud
from database.database import engine, get_db
from database.base import Base
from database.auth_user import UserUseCases
from app.schemas.schemas import User

# Cria as tabelas no banco de dados
Base.metadata.create_all(bind=engine)
from database.database import create_tables

create_tables()  # Garante que as tabelas sejam criadas antes de iniciar o app


app = FastAPI()
templates = Jinja2Templates(directory="templates")

#Se acessar sem rotas, redireciona para alunos
@app.get("/")
def home(request: Request):
    return RedirectResponse(url="/alunos", status_code=303)

# Rotas para Alunos
@app.get("/alunos")
def listar_alunos(request: Request, db: Session = Depends(get_db)):
    alunos = crud.get_alunos(db)
    return templates.TemplateResponse("alunos.html", {"request": request, "alunos": alunos})

@app.get("/alunos/adicionar")
def form_adicionar_aluno(request: Request):

    return templates.TemplateResponse("form_aluno.html", {"request": request})

@app.post("/alunos/adicionar")
def adicionar_aluno(nome: str = Form(...), curso_id: int = Form(...), db: Session = Depends(get_db)):
    aluno = schemas.AlunoCreate(nome=nome, curso_id=curso_id)
    crud.create_aluno(db, aluno)
    return RedirectResponse(url="/alunos", status_code=303)

@app.get("/alunos/editar/{aluno_id}")
def form_editar_aluno(request: Request, aluno_id: int, db: Session = Depends(get_db)):
    aluno = crud.get_aluno(db, aluno_id)
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return templates.TemplateResponse("form_aluno.html", {"request": request, "aluno": aluno})

@app.post("/alunos/editar/{aluno_id}")
def editar_aluno(aluno_id: int, nome: str = Form(...), curso_id: int = Form(...), db: Session = Depends(get_db)):
    aluno = schemas.AlunoUpdate(nome=nome, curso_id=curso_id)
    crud.update_aluno(db, aluno_id, aluno)
    return RedirectResponse(url="/alunos", status_code=303)

@app.get("/alunos/remover/{aluno_id}")
def remover_aluno(aluno_id: int, db: Session = Depends(get_db)):
    crud.delete_aluno(db, aluno_id)
    return RedirectResponse(url="/alunos", status_code=303)

# Rotas para Cursos
@app.get("/cursos")
def listar_cursos(request: Request, db: Session = Depends(get_db)):
    cursos = crud.get_cursos(db)
    return templates.TemplateResponse("cursos.html", {"request": request, "cursos": cursos})

@app.get("/cursos/adicionar")
def form_adicionar_curso(request: Request):
    return templates.TemplateResponse("form_curso.html", {"request": request})

@app.post("/cursos/adicionar")
def adicionar_curso(nome: str = Form(...), descricao: str = Form(...), db: Session = Depends(get_db)):
    curso = schemas.CursoCreate(nome=nome, descricao=descricao)
    crud.create_curso(db, curso)
    return RedirectResponse(url="/cursos", status_code=303)

@app.get("/cursos/editar/{curso_id}")
def form_editar_curso(request: Request, curso_id: int, db: Session = Depends(get_db)):
    curso = crud.get_curso(db, curso_id)
    if not curso:
        raise HTTPException(status_code=404, detail="Curso não encontrado")
    return templates.TemplateResponse("form_curso.html", {"request": request, "curso": curso})

@app.post("/cursos/editar/{curso_id}")
def editar_curso(curso_id: int, nome: str = Form(...), descricao: str = Form(...), db: Session = Depends(get_db)):
    curso = schemas.CursoUpdate(nome=nome, descricao=descricao)
    crud.update_curso(db, curso_id, curso)
    return RedirectResponse(url="/cursos", status_code=303)

@app.get("/cursos/remover/{curso_id}")
def remover_curso(curso_id: int, db: Session = Depends(get_db)):
    crud.delete_curso(db, curso_id)
    return RedirectResponse(url="/cursos", status_code=303)

# Rotas para Professores
@app.get("/professores")
def listar_professores(request: Request, db: Session = Depends(get_db)):
    professores = crud.get_professores(db)
    return templates.TemplateResponse("professores.html", {"request": request, "professores": professores})

@app.get("/professores/adicionar")
def form_adicionar_professor(request: Request):
    return templates.TemplateResponse("form_professor.html", {"request": request})

@app.post("/professores/adicionar")
def adicionar_professor(nome: str = Form(...), especializacao: str = Form(...), departamento: str = Form(...), db: Session = Depends(get_db)):
    professor = schemas.ProfessorCreate(nome=nome, especializacao=especializacao, departamento=departamento)
    crud.create_professor(db, professor)
    return RedirectResponse(url="/professores", status_code=303)

@app.get("/professores/editar/{professor_id}")
def form_editar_professor(request: Request, professor_id: int, db: Session = Depends(get_db)):
    professor = crud.get_professor(db, professor_id)
    if not professor:
        raise HTTPException(status_code=404, detail="Professor não encontrado")
    return templates.TemplateResponse("form_professor.html", {"request": request, "professor": professor})

@app.post("/professores/editar/{professor_id}")
def editar_professor(professor_id: int, nome: str = Form(...), especializacao: str = Form(...), departamento: str = Form(...), db: Session = Depends(get_db)):
    professor = schemas.ProfessorUpdate(nome=nome, especializacao=especializacao, departamento=departamento)
    crud.update_professor(db, professor_id, professor)
    return RedirectResponse(url="/professores", status_code=303)

@app.get("/professores/remover/{professor_id}")
def remover_professor(professor_id: int, db: Session = Depends(get_db)):
    crud.delete_professor(db, professor_id)
    return RedirectResponse(url="/professores", status_code=303)

@app.get("/login")
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/register")
def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.post("/login")
def user_login(
    request_form_user: OAuth2PasswordRequestForm= Depends(),
    db: Session= Depends(get_db)
):
    uc= UserUseCases(db_session=db)
    user= User(
        username= request_form_user.username,
        password= request_form_user.password
    )

    auth_data= uc.user_login(user=user)
    return {
        "content": auth_data,
        "status_code": status.HTTP_200_OK
    }

# Rota para cadastro de usuário
@app.post("/register")
async def user_register(
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    # Criar objeto do usuário
    user = User(username=username, password=password)

    # Salvar usuário no banco de dados
    uc = UserUseCases(db_session=db)
    uc.user_register(user=user)

    # Redirecionar para a página de login
    return RedirectResponse(url="/login", status_code=303)

# Rota para login de usuário
@app.post("/login")
def user_login(
    request_form_user: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    uc = UserUseCases(db_session=db)
    user = User(
        username=request_form_user.username,
        password=request_form_user.password
    )
    auth_data = uc.user_login(user=user)
    # Após o login, redireciona para uma rota protegida (exemplo: /alunos)
    response = RedirectResponse(url="/alunos", status_code=303)
    # Opcional: Armazena o token JWT em um cookie HTTP-only
    response.set_cookie(key="access_token", value=auth_data["access_token"], httponly=True)
    return response