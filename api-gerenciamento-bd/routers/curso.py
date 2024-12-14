from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
import models, schemas
from database import get_db

router = APIRouter()

@router.get("/", response_model=list[schemas.CursoResponseSchema])
def listar_cursos(db: Session = Depends(get_db)):
    return db.query(models.Curso).all()

@router.post("/", response_model=schemas.CursoResponseSchema, status_code=status.HTTP_201_CREATED)
def criar_curso(payload: schemas.CursoBaseSchema, db: Session = Depends(get_db)):
    return payload.criar_curso(db)

@router.put("/{curso_id}", response_model=schemas.CursoResponseSchema)
def atualizar_curso(curso_id: int, payload: schemas.CursoBaseSchema, db: Session = Depends(get_db)):
    curso = db.query(models.Curso).filter(models.Curso.id == curso_id).first()
    if not curso:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")
    return payload.atualizar_curso(curso, db)

@router.delete("/{curso_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_curso(curso_id: int, db: Session = Depends(get_db)):
    curso = db.query(models.Curso).filter(models.Curso.id == curso_id).first()
    if not curso:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")
    db.delete(curso)
    db.commit()
