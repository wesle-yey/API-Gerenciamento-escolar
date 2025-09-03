from fastapi import APIRouter, Depends, HTTPException, Request, Form
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
import crud
from app.schemas.schemas import CursoCreate, CursoUpdate
from database.database import get_db
from fastapi.templating import Jinja2Templates

from database.token import verify_token

router = APIRouter(dependencies=[Depends(verify_token)])
templates = Jinja2Templates(directory="templates")

@router.get("/cursos")
def listar_cursos(request: Request, db: Session = Depends(get_db)):
    cursos = crud.get_cursos(db)
    return templates.TemplateResponse("cursos.html", {"request": request, "cursos": cursos})

@router.get("/cursos/adicionar")
def form_adicionar_curso(request: Request):
    return templates.TemplateResponse("form_curso.html", {"request": request})

@router.post("/cursos/adicionar")
def adicionar_curso(nome: str = Form(...), descricao: str = Form(...), db: Session = Depends(get_db)):
    curso = CursoCreate(nome=nome, descricao=descricao)
    crud.create_curso(db, curso)
    return RedirectResponse(url="/cursos", status_code=303)

@router.get("/cursos/editar/{curso_id}")
def form_editar_curso(request: Request, curso_id: int, db: Session = Depends(get_db)):
    curso = crud.get_curso(db, curso_id)
    if not curso:
        raise HTTPException(status_code=404, detail="Curso não encontrado")
    return templates.TemplateResponse("form_curso.html", {"request": request, "curso": curso})

@router.post("/cursos/editar/{curso_id}")
def editar_curso(curso_id: int, nome: str = Form(...), descricao: str = Form(...), db: Session = Depends(get_db)):
    curso = CursoUpdate(nome=nome, descricao=descricao)
    crud.update_curso(db, curso_id, curso)
    return RedirectResponse(url="/cursos", status_code=303)

@router.get("/cursos/remover/{curso_id}")
def remover_curso(curso_id: int, db: Session = Depends(get_db)):
    crud.delete_curso(db, curso_id)
    return RedirectResponse(url="/cursos", status_code=303)
