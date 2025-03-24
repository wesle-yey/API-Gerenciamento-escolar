from fastapi import APIRouter, Depends, Request, Form
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
import crud
from app.schemas.schemas import AlunoCreate, AlunoUpdate
from database.database import get_db
from fastapi.templating import Jinja2Templates
from database.token import verify_token

router = APIRouter(dependencies=[Depends(verify_token)])  # 🔒 Todas as rotas exigem token

templates = Jinja2Templates(directory="templates")

@router.get("/alunos")
def listar_alunos(request: Request, db: Session = Depends(get_db)):
    alunos = crud.get_alunos(db)
    return templates.TemplateResponse("alunos.html", {"request": request, "alunos": alunos})

@router.post("/alunos/adicionar")
def adicionar_aluno(nome: str = Form(...), curso_id: int = Form(...), db: Session = Depends(get_db)):
    aluno = AlunoCreate(nome=nome, curso_id=curso_id)
    crud.create_aluno(db, aluno)
    return RedirectResponse(url="/alunos", status_code=303)
