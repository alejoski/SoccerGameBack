from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
from src.v1.models import usuario
from src.v1.setting.database import engine,  get_db
from sqlalchemy.orm import Session

from src.v1.setting import database


app = FastAPI()

database.Base.metadata.create_all(bind=engine)

class UsuarioBase(BaseModel):
        user_name:str

    

        
db_dependency = Annotated[Session, Depends(get_db)]
        

@app.get("/")
async def root():
    return {"message":"Hello World"}

@app.post("/user/", status_code=status.HTTP_201_CREATED)
async def create_user(user:UsuarioBase, db:db_dependency):
    db_user = usuario.Usario(**user.model_dump())#model_dump-dict
    db.add(user)
    db.commit()