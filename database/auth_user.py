from fastapi import status
from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.models.models import User
from app.schemas import UserBase
from passlib.context import CryptContext

crypt_context= CryptContext(schemes=['sha256_crypt'])

class UserUseCases:
    def __init__(self, db_session: Session):
        self.db_session= db_session

    def user_register(self, user: UserBase):
        user_model= User(
            username= user.username,
            password= crypt_context.hash(user.password)
        )
        try:
            self.db_session.add(user)
            self.db_session.commit()
        except IntegrityError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='User already exists'
            )