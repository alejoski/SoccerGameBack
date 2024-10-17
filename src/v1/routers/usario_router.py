from unittest import result
from fastapi import APIRouter, status, Depends
from typing import Annotated, List

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from src.v1.setting.database import get_db

from src.v1.models.usuario_model import Usuario as UsuarioModel
from src.v1.dao_services.usuario_services import UsusarioServices
from src.v1.dto_schemas.usuario_dto import UsuarioDTO, UsuarioLoginDTO
from src.v1.setting.jwt_manager import create_token
from src.v1.middlewares.jwt_bearer import JWTBearer


router = APIRouter(prefix="/usuarios", tags=["usuarios"])

db_dependency = Annotated[Session, Depends(get_db)]


@router.post('/login', tags=['auth'])
def login(db: db_dependency, usuario:UsuarioLoginDTO):

    result = UsusarioServices(db).get_usuario_by_email(usuario.email)

    print("RESULTADO BD")
    print(usuario.email, result.email)
    print(usuario.password, result.password)

    if not result:
        return JSONResponse(status_code=404, content={"message":"Usuario no encontrado"})
    
    

    if usuario.email == result.email and  usuario.password == result.password:
        token : str = create_token(usuario.dict())
        

        return JSONResponse(status_code=200, content=jsonable_encoder({"token":token}))



@router.post("/newUser", status_code=status.HTTP_201_CREATED)
async def create_user(user: UsuarioDTO, db: db_dependency):
    UsusarioServices(db).create_usuario(user)



@router.get("/getUser", dependencies=[Depends(JWTBearer())])
def get_users(db: db_dependency) -> List[UsuarioDTO]:
    result = UsusarioServices(db).get_usuarios()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))



@router.get("/getUserByEmail/{email}", response_model=UsuarioDTO)
def get_user_by_email(email:str, db:db_dependency)-> UsuarioDTO:
    print("Llego al router get_user_by_email()", email)
    result = UsusarioServices(db).get_usuario_by_email(email)
    return JSONResponse(status_code=200, content=jsonable_encoder(result))
