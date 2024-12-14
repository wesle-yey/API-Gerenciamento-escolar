from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
import models, schemas
from database import get_db

router = APIRouter()

# Rota GET para listar professores
@router.get("/", response_model=list[schemas.ProfessorResponseSchema])
def listar_professores(db: Session = Depends(get_db)):
    return db.query(models.Professor).all()

# Rota POST para criar um novo professor
@router.post("/", response_model=schemas.ProfessorResponseSchema, status_code=status.HTTP_201_CREATED)
def criar_professor(payload: schemas.ProfessorBaseSchema, db: Session = Depends(get_db)):
    return payload.criar_professor(db)

# Rota PUT para atualizar um professor
@router.put("/{professor_id}", response_model=schemas.ProfessorResponseSchema)
def atualizar_professor(professor_id: int, payload: schemas.ProfessorBaseSchema, db: Session = Depends(get_db)):
    professor = db.query(models.Professor).filter(models.Professor.id == professor_id).first()
    if not professor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Professor não encontrado")
    return payload.atualizar_professor(professor, db)

# Rota DELETE para deletar um professor
@router.delete("/{professor_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_professor(professor_id: int, db: Session = Depends(get_db)):
    professor = db.query(models.Professor).filter(models.Professor.id == professor_id).first()
    if not professor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Professor não encontrado")
    db.delete(professor)
    db.commit()
