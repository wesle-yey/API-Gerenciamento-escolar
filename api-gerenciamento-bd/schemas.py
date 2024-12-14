from pydantic import BaseModel, Field
from typing import Optional
from sqlalchemy.orm import Session
import models

# Schema base para Aluno
class AlunoBaseSchema(BaseModel):
    nome: str = Field(..., min_length=1, max_length=100)
    curso_id: int

    def criar_aluno(self, db: Session):
        novo_aluno = models.Aluno(**self.dict())
        db.add(novo_aluno)
        db.commit()
        db.refresh(novo_aluno)
        return novo_aluno

    def atualizar_aluno(self, aluno: models.Aluno, db: Session):
        for key, value in self.dict(exclude_unset=True).items():
            setattr(aluno, key, value)
        db.commit()
        db.refresh(aluno)
        return aluno

# Schema de resposta para Aluno (inclui o ID)
class AlunoResponseSchema(AlunoBaseSchema):
    id: int

    class Config:
        orm_mode = True

# Schema base para Curso
class CursoBaseSchema(BaseModel):
    nome: str = Field(..., min_length=1, max_length=100)
    descricao: Optional[str]

    def criar_curso(self, db: Session):
        novo_curso = models.Curso(**self.dict())
        db.add(novo_curso)
        db.commit()
        db.refresh(novo_curso)
        return novo_curso

    def atualizar_curso(self, curso: models.Curso, db: Session):
        for key, value in self.dict(exclude_unset=True).items():
            setattr(curso, key, value)
        db.commit()
        db.refresh(curso)
        return curso

# Schema de resposta para Curso (inclui o ID)
class CursoResponseSchema(CursoBaseSchema):
    id: int

    class Config:
        orm_mode = True

# Schema base para Professor
class ProfessorBaseSchema(BaseModel):
    nome: str = Field(..., min_length=1, max_length=100)
    especializacao: str
    departamento: str

    def criar_professor(self, db: Session):
        novo_professor = models.Professor(**self.dict())
        db.add(novo_professor)
        db.commit()
        db.refresh(novo_professor)
        return novo_professor

    def atualizar_professor(self, professor: models.Professor, db: Session):
        for key, value in self.dict(exclude_unset=True).items():
            setattr(professor, key, value)
        db.commit()
        db.refresh(professor)
        return professor

# Schema de resposta para Professor (inclui o ID)
class ProfessorResponseSchema(ProfessorBaseSchema):
    id: int

    class Config:
        orm_mode = True
