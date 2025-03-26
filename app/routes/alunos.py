from fastapi import APIRouter, Depends, HTTPException, Request, Form
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from app.models.models import UserModel
from app.schemas import schemas
import crud
from app.schemas.schemas import AlunoCreate, AlunoUpdate
from database.database import get_db
from fastapi.templating import Jinja2Templates
from database.token import verify_token

router = APIRouter(dependencies=[Depends(verify_token)])  # 🔒 Todas as rotas exigem token

templates = Jinja2Templates(directory="templates")

# Rotas para Alunos
@router.get("/alunos")
def listar_alunos(request: Request, db: Session = Depends(get_db), user: UserModel = Depends(verify_token)):
    alunos = crud.get_alunos(db)
    return templates.TemplateResponse("alunos.html", {"request": request, "alunos": alunos})

@router.get("/alunos/adicionar")
def form_adicionar_aluno(request: Request, db: Session = Depends(get_db)):
    cursos = crud.get_cursos(db)  # Busca todos os cursos do banco
    return templates.TemplateResponse("form_aluno.html", {"request": request, "cursos": cursos})

@router.post("/alunos/adicionar")
def adicionar_aluno(nome: str = Form(...), curso_id: int = Form(...), db: Session = Depends(get_db)):
    aluno = schemas.AlunoCreate(nome=nome, curso_id=curso_id)
    crud.create_aluno(db, aluno)
    return RedirectResponse(url="/alunos", status_code=303)

@router.get("/alunos/editar/{aluno_id}")
def form_editar_aluno(request: Request, aluno_id: int, db: Session = Depends(get_db)):
    aluno = crud.get_aluno(db, aluno_id)
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    
    cursos = crud.get_cursos(db)  # Busca todos os cursos
    return templates.TemplateResponse("form_aluno.html", {"request": request, "aluno": aluno, "cursos": cursos})

@router.post("/alunos/editar/{aluno_id}")
def editar_aluno(aluno_id: int, nome: str = Form(...), curso_id: int = Form(...), db: Session = Depends(get_db)):
    aluno = schemas.AlunoUpdate(nome=nome, curso_id=curso_id)
    crud.update_aluno(db, aluno_id, aluno)
    return RedirectResponse(url="/alunos", status_code=303)

@router.get("/alunos/remover/{aluno_id}")
def remover_aluno(aluno_id: int, db: Session = Depends(get_db)):
    crud.delete_aluno(db, aluno_id)
    return RedirectResponse(url="/alunos", status_code=303)