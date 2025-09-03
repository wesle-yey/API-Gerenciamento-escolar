from pydantic import BaseModel, Field, field_validator
import re

# Schemas para Aluno
class AlunoBase(BaseModel):
    nome: str = Field(..., min_length=2, max_length=100, description="Nome do aluno")
    curso_id: int = Field(..., gt=0, description="ID do curso")

    @field_validator('nome')
    @classmethod
    def validate_nome(cls, v):
        if not v or not v.strip():
            raise ValueError('Nome não pode estar vazio')
        # Remover caracteres especiais perigosos
        v = re.sub(r'[<>"\']', '', v.strip())
        if len(v) < 2:
            raise ValueError('Nome deve ter pelo menos 2 caracteres')
        return v

class AlunoCreate(AlunoBase):
    pass

class AlunoUpdate(AlunoBase):
    pass

# Schemas para Curso
class CursoBase(BaseModel):
    nome: str = Field(..., min_length=2, max_length=100, description="Nome do curso")
    descricao: str = Field(..., min_length=5, max_length=255, description="Descrição do curso")

    @field_validator('nome')
    @classmethod
    def validate_nome(cls, v):
        if not v or not v.strip():
            raise ValueError('Nome não pode estar vazio')
        v = re.sub(r'[<>"\']', '', v.strip())
        if len(v) < 2:
            raise ValueError('Nome deve ter pelo menos 2 caracteres')
        return v

    @field_validator('descricao')
    @classmethod
    def validate_descricao(cls, v):
        if not v or not v.strip():
            raise ValueError('Descrição não pode estar vazia')
        v = re.sub(r'[<>"\']', '', v.strip())
        if len(v) < 5:
            raise ValueError('Descrição deve ter pelo menos 5 caracteres')
        return v

class CursoCreate(CursoBase):
    pass

class CursoUpdate(CursoBase):
    pass

# Schemas para Professor
class ProfessorBase(BaseModel):
    nome: str = Field(..., min_length=2, max_length=100, description="Nome do professor")
    especializacao: str = Field(..., min_length=2, max_length=150, description="Especialização")
    departamento: str = Field(..., min_length=2, max_length=100, description="Departamento")

    @field_validator('nome')
    @classmethod
    def validate_nome(cls, v):
        if not v or not v.strip():
            raise ValueError('Nome não pode estar vazio')
        v = re.sub(r'[<>"\']', '', v.strip())
        if len(v) < 2:
            raise ValueError('Nome deve ter pelo menos 2 caracteres')
        return v

    @field_validator('especializacao')
    @classmethod
    def validate_especializacao(cls, v):
        if not v or not v.strip():
            raise ValueError('Especialização não pode estar vazia')
        v = re.sub(r'[<>"\']', '', v.strip())
        if len(v) < 2:
            raise ValueError('Especialização deve ter pelo menos 2 caracteres')
        return v

    @field_validator('departamento')
    @classmethod
    def validate_departamento(cls, v):
        if not v or not v.strip():
            raise ValueError('Departamento não pode estar vazio')
        v = re.sub(r'[<>"\']', '', v.strip())
        if len(v) < 2:
            raise ValueError('Departamento deve ter pelo menos 2 caracteres')
        return v

class ProfessorCreate(ProfessorBase):
    pass

class ProfessorUpdate(ProfessorBase):
    pass

class User(BaseModel):
    username: str = Field(..., min_length=3, max_length=50, description="Nome de usuário")
    password: str = Field(..., min_length=8, max_length=128, description="Senha")

    @field_validator('username')
    @classmethod
    def validate_username(cls, v):
        if not v or not v.strip():
            raise ValueError('Username não pode estar vazio')
        # Permitir apenas letras, números e underscore
        if not re.match(r'^[a-zA-Z0-9_]+$', v):
            raise ValueError('Username deve conter apenas letras, números e underscore')
        return v.lower().strip()

    @field_validator('password')
    @classmethod
    def validate_password(cls, v):
        if not v or len(v) < 8:
            raise ValueError('Senha deve ter pelo menos 8 caracteres')
        # Verificar se tem pelo menos uma letra e um número
        if not re.search(r'[A-Za-z]', v) or not re.search(r'\d', v):
            raise ValueError('Senha deve conter pelo menos uma letra e um número')
        return v

