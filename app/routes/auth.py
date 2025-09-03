from fastapi import APIRouter, Depends, Form, Request, HTTPException, status
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from database.auth_user import UserUseCases
from app.schemas.schemas import User
from database.database import get_db
from fastapi.templating import Jinja2Templates
from database.token import logout
from fastapi.security import OAuth2PasswordRequestForm
import os

router = APIRouter()
templates = Jinja2Templates(directory="templates")  # 📁 Diretório de templates

@router.post("/api/login")
def api_login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    uc = UserUseCases(db_session=db)
    user = User(username=form_data.username, password=form_data.password)
    try:
        auth_data = uc.user_login(user=user)
        access_token = auth_data["access_token"]
        return {
            "access_token": access_token,
            "token_type": "bearer"
        }
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))
        
# 🔹 Rota GET para exibir a página de login
@router.get("/login")
def login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

# 🔹 Rota POST para processar o login
@router.post("/login")
def user_login(
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    try:
        uc = UserUseCases(db_session=db)
        user = User(username=username, password=password)
        auth_data = uc.user_login(user=user)
        access_token = auth_data["access_token"]
        
        response = RedirectResponse(url="/alunos", status_code=303)
        # Determinar se está em produção baseado na variável de ambiente
        is_production = os.getenv("ENVIRONMENT", "development") == "production"
        
        response.set_cookie(
            key="access_token",
            value=access_token,
            httponly=True,
            secure=is_production,  # HTTPS apenas em produção
            max_age=30 * 60,
            expires=30 * 60,
            samesite="lax"
        )
        return response
    except Exception as e:
        # Em caso de erro, redirecionar para login com mensagem
        return RedirectResponse(url="/login?error=invalid_credentials", status_code=303)

# 🔹 Rota GET para exibir a página de registro
@router.get("/register")
def register_form(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

# 🔹 Rota POST para processar o registro
@router.post("/register")
async def user_register(
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    try:
        user = User(username=username, password=password)
        uc = UserUseCases(db_session=db)
        uc.user_register(user=user)
        return RedirectResponse(url="/login", status_code=303)
    except Exception as e:
        # Em caso de erro, redirecionar para registro com mensagem
        return RedirectResponse(url="/register?error=registration_failed", status_code=303)

@router.get("/logout")
def logout_system(request: Request):
    return logout(request)
