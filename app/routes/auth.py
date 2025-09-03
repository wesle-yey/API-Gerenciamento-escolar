from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from database.auth_user import UserUseCases
from app.schemas.schemas import User
from database.database import get_db
from fastapi.templating import Jinja2Templates
from database.token import logout

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
    uc = UserUseCases(db_session=db)
    user = User(username=username, password=password)
    auth_data = uc.user_login(user=user)
    access_token = auth_data["access_token"]
    
    response = RedirectResponse(url="/alunos", status_code=303)
    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        secure=False,
        max_age=30 * 60,
        expires=30 * 60,
        samesite="lax"
    )
    return response

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
    user = User(username=username, password=password)
    uc = UserUseCases(db_session=db)
    uc.user_register(user=user)
    return RedirectResponse(url="/login", status_code=303)

@router.get("/logout")
def logout_system(request: Request):
    return logout(request)
