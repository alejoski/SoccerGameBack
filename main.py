from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
import model
from database import engine, SessionLocal
from sqlalchemy.orm import Session


app = FastAPI()

model.Base.metadata.create_all(bind=engine)

class UsuarioBase(BaseModel):
        user_name:str

    
def get_db():
    db = SessionLocal()        
    try:
        yield db
    finally:
        db.close()
        
db_dependency = Annotated[Session, Depends(get_db)]
        

@app.get("/")
async def root():
    return {"message":"Hello World"}

@app.post("/user/", status_code=status.HTTP_201_CREATED)
async def create_user(user:UsuarioBase, db:db_dependency):
    db_user = model.model.Usario(**user.dict())
    db.add(user)
    db.commit()