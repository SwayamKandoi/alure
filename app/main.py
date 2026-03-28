from fastapi import FastAPI

from app.db.database import Base, engine
from app.routes import clothing

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(clothing.router)

@app.get("/")
def read_root():
    return {"message": "Alure backend is running"}