from fastapi import APIRouter, Depends, status
from typing import Annotated
from sqlalchemy.orm import Session

from src.v1.setting.database import  get_db
from src.v1.models.juego_model import Jugadas


router =  APIRouter(prefix="/jugadas", tags=["jugadas"])

db_dependency = Annotated[Session, Depends(get_db)]

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_juego(db: db_dependency):
    # db_user = usuario.Usario(**user.model_dump())#model_dump-dict

    # db = Session()
    new_user = Jugadas()

    db.add(new_user)
    db.commit()
