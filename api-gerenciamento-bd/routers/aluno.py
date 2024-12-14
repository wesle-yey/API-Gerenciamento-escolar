from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
import models, schemas
from database import get_db

router = APIRouter()

# Rota GET para listar alunos
@router.get("/", response_model=list[schemas.AlunoResponseSchema])
def listar_alunos(db: Session = Depends(get_db)):
    return db.query(models.Aluno).all()

# Rota POST para criar um novo aluno
@router.post("/", response_model=schemas.AlunoResponseSchema, status_code=status.HTTP_201_CREATED)
def criar_aluno(payload: schemas.AlunoBaseSchema, db: Session = Depends(get_db)):
    return payload.criar_aluno(db)

# Rota PUT para atualizar um aluno
@router.put("/{aluno_id}", response_model=schemas.AlunoResponseSchema)
def atualizar_aluno(aluno_id: int, payload: schemas.AlunoBaseSchema, db: Session = Depends(get_db)):
    aluno = db.query(models.Aluno).filter(models.Aluno.id == aluno_id).first()
    if not aluno:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Aluno não encontrado")
    return payload.atualizar_aluno(aluno, db)

# Rota DELETE para deletar um aluno
@router.delete("/{aluno_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_aluno(aluno_id: int, db: Session = Depends(get_db)):
    aluno = db.query(models.Aluno).filter(models.Aluno.id == aluno_id).first()
    if not aluno:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Aluno não encontrado")
    db.delete(aluno)
    db.commit()
