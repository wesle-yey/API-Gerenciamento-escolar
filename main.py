from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from app.routes import alunos, cursos, professores, auth
from database.database import create_tables  # Import create_tables
import os

app = FastAPI(
    title="API Gerenciamento Escolar",
    description="API para gerenciamento de cursos, alunos e professores",
    version="1.0.0"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("CORS_ORIGINS", "http://localhost:3000,http://localhost:8000").split(","),
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# Create database tables on startup
try:
    create_tables()
    print("✅ Tabelas do banco de dados criadas com sucesso")
except Exception as e:
    print(f"⚠️ Erro ao criar tabelas: {e}")
    # Continuar mesmo com erro para não quebrar a aplicação

# Include routers
app.include_router(alunos.router)
app.include_router(cursos.router)
app.include_router(auth.router)
app.include_router(professores.router)

# Middleware para logging de requisições
@app.middleware('http')
async def logging_middleware(request: Request, call_next):
    # Log da requisição
    print(f"Requisição: {request.method} {request.url}")
    
    response = await call_next(request)
    
    # Log da resposta
    print(f"Resposta: {response.status_code}")
    
    return response

@app.get("/")
def home():
    return RedirectResponse(url="/alunos", status_code=303)

@app.get("/health")
def health_check():
    """Endpoint para health check do Docker"""
    return {"status": "healthy", "message": "API funcionando corretamente"}