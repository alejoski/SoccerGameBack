from unittest import result
from fastapi import APIRouter, status, Depends
from typing import Annotated, List

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from pydantic import BaseModel
from src.v1.setting.database import get_db

from src.v1.models.usuario_model import Usuario as UsuarioModel
from src.v1.services.usuario_services import UsusarioServices



router = APIRouter(prefix="/usuarios", tags=["usuarios"])

db_dependency = Annotated[Session, Depends(get_db)]


class UsuarioBase(BaseModel):
    id: int
    user_name: str


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(user: UsuarioBase, db: db_dependency):
    # db_user = usuario.Usario(**user.model_dump())#model_dump-dict
    # db = Session()
    new_user = UsuarioModel(**user.model_dump())
    db.add(new_user)
    db.commit()

@router.get('/')
def get_users(db: db_dependency) -> List[UsuarioBase]:    
    result = UsusarioServices(db).get_usuarios()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


