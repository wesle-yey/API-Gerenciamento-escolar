from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from app.routes import alunos, cursos, professores, auth
from database.database import create_tables  # Import create_tables

app = FastAPI()

# Create database tables on startup
create_tables()

# Include routers
app.include_router(alunos.router)
app.include_router(cursos.router)
app.include_router(auth.router)
app.include_router(professores.router)

# Middleware
@app.middleware('http')
async def middleware_login(request: Request, call_next):
    response = await call_next(request)
    if response.status_code == 401:
        print("Requisição não autorizada (401)")
        return RedirectResponse("/login")
    return response

@app.get("/")
def home():
    return RedirectResponse(url="/alunos", status_code=303)