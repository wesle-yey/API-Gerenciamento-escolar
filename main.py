from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.routes import alunos, cursos, professores, auth
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

# Inclui os módulos de rotas
app.include_router(alunos.router)
app.include_router(cursos.router)
app.include_router(auth.router)
app.include_router(professores.router)

@app.get("/")
def home():
    return RedirectResponse(url="/alunos", status_code=303)
