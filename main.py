from typing import List

from fastapi import FastAPI, Form, HTTPException, Query

app = FastAPI()

# "Banco de dados" em memória
cursos = []
alunos = []
professores = []

# --- CURSOS ---
@app.get("/cursos")
async def list_cursos():
    return {"status": "success", "message": "Cursos retrieved successfully.", "data": cursos}

@app.get("/cursos/{curso_id}")
async def get_curso_by_id(curso_id: int):
    for curso in cursos:
        if curso["id"] == curso_id:
            return {"status": "success", "message": "Curso retrieved successfully.", "data": curso}
    raise HTTPException(status_code=404, detail="Curso not found.")

@app.post("/cursos")
async def create_curso(nome: str = Form(...), descricao: str = Form(...)):
    curso = {"id": len(cursos) + 1, "nome": nome, "descricao": descricao}
    cursos.append(curso)
    return {"status": "success", "message": "Curso added successfully.", "data": curso}

@app.put("/cursos/{curso_id}")
async def update_curso(curso_id: int, nome: str = Form(...), descricao: str = Form(...)):
    for curso in cursos:
        if curso["id"] == curso_id:
            curso.update({"nome": nome, "descricao": descricao})
            return {"status": "success", "message": "Curso updated successfully.", "data": curso}
    raise HTTPException(status_code=404, detail="Curso not found.")

@app.delete("/cursos/{curso_id}")
async def delete_curso(curso_id: int):
    for index, curso in enumerate(cursos):
        if curso["id"] == curso_id:
            deleted_curso = cursos.pop(index)
            return {"status": "success", "message": "Curso deleted successfully.", "data": deleted_curso}
    raise HTTPException(status_code=404, detail="Curso not found.")

# --- ALUNOS ---
@app.get("/alunos")
async def list_alunos():
    return {"status": "success", "message": "Alunos retrieved successfully.", "data": alunos}

@app.get("/alunos/{aluno_id}")
async def get_aluno_by_id(aluno_id: int):
    for aluno in alunos:
        if aluno["id"] == aluno_id:
            return {"status": "success", "message": "Aluno retrieved successfully.", "data": aluno}
    raise HTTPException(status_code=404, detail="Aluno not found.")

@app.post("/alunos")
async def create_aluno(nome: str = Form(...), email: str = Form(...), curso_id: int = Form(...)):
    aluno = {"id": len(alunos) + 1, "nome": nome, "email": email, "curso_id": curso_id}
    alunos.append(aluno)
    return {"status": "success", "message": "Aluno added successfully.", "data": aluno}

@app.put("/alunos/{aluno_id}")
async def update_aluno(aluno_id: int, nome: str = Form(...), email: str = Form(...), curso_id: int = Form(...)):
    for aluno in alunos:
        if aluno["id"] == aluno_id:
            aluno.update({"nome": nome, "email": email, "curso_id": curso_id})
            return {"status": "success", "message": "Aluno updated successfully.", "data": aluno}
    raise HTTPException(status_code=404, detail="Aluno not found.")

@app.delete("/alunos/{aluno_id}")
async def delete_aluno(aluno_id: int):
    for index, aluno in enumerate(alunos):
        if aluno["id"] == aluno_id:
            deleted_aluno = alunos.pop(index)
            return {"status": "success", "message": "Aluno deleted successfully.", "data": deleted_aluno}
    raise HTTPException(status_code=404, detail="Aluno not found.")

# --- PROFESSORES ---
@app.get("/professores")
async def list_professores():
    return {"status": "success", "message": "Professores retrieved successfully.", "data": professores}

@app.get("/professores/{professor_id}")
async def get_professor_by_id(professor_id: int):
    for professor in professores:
        if professor["id"] == professor_id:
            return {"status": "success", "message": "Professor retrieved successfully.", "data": professor}
    raise HTTPException(status_code=404, detail="Professor not found.")

@app.post("/professores")
async def create_professor(nome: str = Form(...), especializacao: str = Form(...), departamento: str = Form(...)):
    professor = {"id": len(professores) + 1, "nome": nome, "especializacao": especializacao, "departamento": departamento}
    professores.append(professor)
    return {"status": "success", "message": "Professor added successfully.", "data": professor}

@app.put("/professores/{professor_id}")
async def update_professor(professor_id: int, nome: str = Form(...), especializacao: str = Form(...), departamento: str = Form(...)):
    for professor in professores:
        if professor["id"] == professor_id:
            professor.update({"nome": nome, "especializacao": especializacao, "departamento": departamento})
            return {"status": "success", "message": "Professor updated successfully.", "data": professor}
    raise HTTPException(status_code=404, detail="Professor not found.")

@app.delete("/professores/{professor_id}")
async def delete_professor(professor_id: int):
    for index, professor in enumerate(professores):
        if professor["id"] == professor_id:
            deleted_professor = professores.pop(index)
            return {"status": "success", "message": "Professor deleted successfully.", "data": deleted_professor}
    raise HTTPException(status_code=404, detail="Professor not found.")
