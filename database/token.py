from fastapi import Depends, HTTPException, Request, status
from fastapi.security import OAuth2PasswordBearer
from app.models.models import UserModel
from database.auth_user import ALGORITHM, SECRET_KEY
from sqlalchemy.orm import Session
from database.database import get_db
from jose import jwt, JWTError

oauth_scheme = OAuth2PasswordBearer(tokenUrl='/login')

def verify_token(request: Request, db: Session = Depends(get_db)):
    # Tenta obter o token do cookie
    token = request.cookies.get("access_token")
    
    # Se não encontrar no cookie, tenta obter pelo header Authorization
    if not token:
        auth_header = request.headers.get("Authorization")
        if auth_header and auth_header.startswith("Bearer "):
            token = auth_header.split(" ")[1]
    
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token não fornecido")
    
    try:
        # Decodifica o token; jwt.decode já verifica a expiração se o campo "exp" estiver presente
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if not username:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido")
        
        # Busca o usuário no banco de dados
        user = db.query(UserModel).filter(UserModel.username == username).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuário não encontrado")
        
        # Retorna o objeto de usuário para ser usado nas rotas protegidas
        return user

    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido ou expirado")
