
from fastapi import APIRouter, Depends, Form, HTTPException, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.schemas import schemas
import crud
from database.database import SessionLocal, get_db
from database.token import verify_token

router = APIRouter(dependencies=[Depends(verify_token)])
templates = Jinja2Templates(directory="templates")

# Rotas para Professores
@router.get("/professores")
def listar_professores(request: Request, db: Session = Depends(get_db)):
    professores = crud.get_professores(db)
    return templates.TemplateResponse("professores.html", {"request": request, "professores": professores})

@router.get("/professores/adicionar")
def form_adicionar_professor(request: Request):
    return templates.TemplateResponse("form_professor.html", {"request": request})

@router.post("/professores/adicionar")
def adicionar_professor(nome: str = Form(...), especializacao: str = Form(...), departamento: str = Form(...), db: Session = Depends(get_db)):
    professor = schemas.ProfessorCreate(nome=nome, especializacao=especializacao, departamento=departamento)
    crud.create_professor(db, professor)
    return RedirectResponse(url="/professores", status_code=303)

@router.get("/professores/editar/{professor_id}")
def form_editar_professor(request: Request, professor_id: int, db: Session = Depends(get_db)):
    professor = crud.get_professor(db, professor_id)
    if not professor:
        raise HTTPException(status_code=404, detail="Professor não encontrado")
    return templates.TemplateResponse("form_professor.html", {"request": request, "professor": professor})

@router.post("/professores/editar/{professor_id}")
def editar_professor(professor_id: int, nome: str = Form(...), especializacao: str = Form(...), departamento: str = Form(...), db: Session = Depends(get_db)):
    professor = schemas.ProfessorUpdate(nome=nome, especializacao=especializacao, departamento=departamento)
    crud.update_professor(db, professor_id, professor)
    return RedirectResponse(url="/professores", status_code=303)

@router.get("/professores/remover/{professor_id}")
def remover_professor(professor_id: int, db: Session = Depends(get_db)):
    crud.delete_professor(db, professor_id)
    return RedirectResponse(url="/professores", status_code=303)