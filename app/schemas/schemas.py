from pydantic import BaseModel

# Schemas para Aluno
class AlunoBase(BaseModel):
    nome: str
    curso_id: int

class AlunoCreate(AlunoBase):
    pass

class AlunoUpdate(AlunoBase):
    pass

# Schemas para Curso
class CursoBase(BaseModel):
    nome: str
    descricao: str

class CursoCreate(CursoBase):
    pass

class CursoUpdate(CursoBase):
    pass

# Schemas para Professor
class ProfessorBase(BaseModel):
    nome: str
    especializacao: str
    departamento: str

class ProfessorCreate(ProfessorBase):
    pass

class ProfessorUpdate(ProfessorBase):
    pass

class UserBase(BaseModel):
    username: str
    password: str

