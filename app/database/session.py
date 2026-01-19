from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings


DATABASE_URL: str = "postgresql+psycopg2://postgres:Kwabena_2002@localhost:5432/businessmgt"


engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def session():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()
