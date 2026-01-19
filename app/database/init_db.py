from app.database.session import engine
from app.database.base import Base
from app.models import transaction3, user3

def init_db():
    Base.metadata.create_all(bind=engine)