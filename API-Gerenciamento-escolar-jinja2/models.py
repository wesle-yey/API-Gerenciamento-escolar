from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from base import Base  # Agora importamos de base.py

class Curso(Base):
    __tablename__ = "cursos"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)  # Definindo tamanho máximo
    descricao = Column(String(255))  # Permite descrições mais longas

    alunos = relationship("Aluno", back_populates="curso")

class Aluno(Base):
    __tablename__ = "alunos"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)  # Nome do aluno com limite de 100 caracteres
    curso_id = Column(Integer, ForeignKey("cursos.id"))

    curso = relationship("Curso", back_populates="alunos")

class Professor(Base):
    __tablename__ = "professores"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)  # Nome do professor limitado a 100 caracteres
    especializacao = Column(String(150), nullable=False)  # Especialização com limite de 150 caracteres
    departamento = Column(String(100), nullable=False)  # Nome do departamento com limite de 100 caracteres
