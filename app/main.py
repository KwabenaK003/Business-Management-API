from fastapi import FastAPI
from app.api.router import api_router
from app.database.init_db import init_db
# from app.api.routes import report1
# from app.api.routes import transaction1
# from app.api.routes import user1

app = FastAPI(
    title="Business Management API",
    version="1.0.0"
)

init_db()
app.include_router(api_router)
# app.include_router(report1)
# app.include_router(transaction1)
# app.include_router(user1)
