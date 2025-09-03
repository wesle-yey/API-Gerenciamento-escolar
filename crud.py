from sqlalchemy.orm import Session, joinedload
import app.models.models as models, app.schemas.schemas as schemas

# CRUD Aluno
def get_alunos(db: Session):
    return db.query(models.Aluno).options(joinedload(models.Aluno.curso)).all()

def get_aluno(db: Session, aluno_id: int):
    return db.query(models.Aluno).options(joinedload(models.Aluno.curso)).filter(models.Aluno.id == aluno_id).first()

def create_aluno(db: Session, aluno: schemas.AlunoCreate):
    db_aluno = models.Aluno(nome=aluno.nome, curso_id=aluno.curso_id)
    db.add(db_aluno)
    db.commit()
    db.refresh(db_aluno)
    return db_aluno

def update_aluno(db: Session, aluno_id: int, aluno: schemas.AlunoUpdate):
    db_aluno = get_aluno(db, aluno_id)
    if db_aluno:
        db_aluno.nome = aluno.nome
        db_aluno.curso_id = aluno.curso_id
        db.commit()
        db.refresh(db_aluno)
    return db_aluno

def delete_aluno(db: Session, aluno_id: int):
    db_aluno = get_aluno(db, aluno_id)
    if db_aluno:
        db.delete(db_aluno)
        db.commit()

# CRUD Curso
def get_cursos(db: Session):
    return db.query(models.Curso).all()

def get_curso(db: Session, curso_id: int):
    return db.query(models.Curso).filter(models.Curso.id == curso_id).first()

def create_curso(db: Session, curso: schemas.CursoCreate):
    db_curso = models.Curso(nome=curso.nome, descricao=curso.descricao)
    db.add(db_curso)
    db.commit()
    db.refresh(db_curso)
    return db_curso

def update_curso(db: Session, curso_id: int, curso: schemas.CursoUpdate):
    db_curso = get_curso(db, curso_id)
    if db_curso:
        db_curso.nome = curso.nome
        db_curso.descricao = curso.descricao
        db.commit()
        db.refresh(db_curso)
    return db_curso

def delete_curso(db: Session, curso_id: int):
    db_curso = get_curso(db, curso_id)
    if db_curso:
        db.delete(db_curso)
        db.commit()

# CRUD Professor
def get_professores(db: Session):
    return db.query(models.Professor).all()

def get_professor(db: Session, professor_id: int):
    return db.query(models.Professor).filter(models.Professor.id == professor_id).first()

def create_professor(db: Session, professor: schemas.ProfessorCreate):
    db_professor = models.Professor(
        nome=professor.nome,
        especializacao=professor.especializacao,
        departamento=professor.departamento
    )
    db.add(db_professor)
    db.commit()
    db.refresh(db_professor)
    return db_professor

def update_professor(db: Session, professor_id: int, professor: schemas.ProfessorUpdate):
    db_professor = get_professor(db, professor_id)
    if db_professor:
        db_professor.nome = professor.nome
        db_professor.especializacao = professor.especializacao
        db_professor.departamento = professor.departamento
        db.commit()
        db.refresh(db_professor)
    return db_professor

def delete_professor(db: Session, professor_id: int):
    db_professor = get_professor(db, professor_id)
    if db_professor:
        db.delete(db_professor)
        db.commit()