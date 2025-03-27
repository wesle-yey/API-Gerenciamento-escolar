from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from app.routes import alunos, cursos, professores, auth

app = FastAPI()

# Inclui os módulos de rotas
app.include_router(alunos.router)
app.include_router(cursos.router)
app.include_router(auth.router)
app.include_router(professores.router)

#atuar no meio da requisição, para verificar se o usuário está logado
@app.middleware('http')
async def middleware_login(request: Request, call_next):
    response = await call_next(request)
    
     # Caso usuário não esteja logado, redireciona para a página de login
    if response.status_code == 401:
        print("Requisição não autorizada (401)")
        return RedirectResponse("/login")
    
    return response

@app.get("/")
def home():
    return RedirectResponse(url="/alunos", status_code=303)
