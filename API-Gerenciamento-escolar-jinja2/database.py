from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base import Base  # Agora importamos de base.py
import models  # Importamos após definir Base

DATABASE_URL = "sqlite:///./test.db"  # Ou sua URL do banco de dados

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Criar as tabelas no banco de dados
def create_tables():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

if __name__ == "__main__":
    create_tables()
