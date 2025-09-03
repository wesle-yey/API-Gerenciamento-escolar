from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.base import Base  # Agora importamos de base.py
import app.models.models as models  # Importamos após definir Base
import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")  # Fallback para SQLite


engine = create_engine(DATABASE_URL, echo=False)

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
