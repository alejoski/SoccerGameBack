from traceback import print_tb
from unittest import result
from xmlrpc.client import Boolean
from fastapi import APIRouter, HTTPException, status, Depends
from typing import Annotated, List

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy import PrimaryKeyConstraint, null
from sqlalchemy.orm import Session

from src.v1.setting.database import get_db

from src.v1.models.usuario_model import Usuario as UsuarioModel
from src.v1.dao_services.usuario_services import UsusarioServices
from src.v1.dto_schemas.usuario_dto import UsuarioDTO, UsuarioLoginDTO
from src.v1.setting.jwt_manager import create_token, validate_token
from src.v1.middlewares.jwt_bearer import JWTBearer


router = APIRouter(prefix="/usuarios", tags=["usuarios"])

db_dependency = Annotated[Session, Depends(get_db)]



@router.post('/login', tags=['auth'])
def login(db: db_dependency, usuario:UsuarioLoginDTO):

    result = UsusarioServices(db).get_usuario_by_email(usuario.email)


    if not result:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user_not_found" )
        #return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, detail="user_not_found")
       

    print("RESULTADO BD")
    print(usuario.email, result.email)
    print(usuario.password, result.password)


    if usuario.email == result.email and  usuario.password == result.password:
        token : str = create_token(usuario.dict())
        result.password = ""
        

        return JSONResponse(status_code=200, content=jsonable_encoder({"token":token, "user": result}))



@router.post("/new", status_code=status.HTTP_201_CREATED)
async def create_user(user: UsuarioDTO, db: db_dependency):  

    result = UsusarioServices(db).get_usuario_by_email(user.email)
    if result:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="user_already_registered")
        #return JSONResponse(status_code=400, content={"message":"User already exists"})
    
    UsusarioServices(db).create_usuario(user)
    return 



@router.get("/getUser", dependencies=[Depends(JWTBearer())])
def get_users(db: db_dependency) -> List[UsuarioDTO]:
    result = UsusarioServices(db).get_usuarios()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))



@router.get("/getUserByEmail/{email}", response_model=UsuarioDTO)
def get_user_by_email(email:str, db:db_dependency)-> UsuarioDTO:
    print("Llego al router get_user_by_email()", email)
    result = UsusarioServices(db).get_usuario_by_email(email)
    return JSONResponse(status_code=200, content=jsonable_encoder(result))






def token_validate( db: db_dependency, token : str = Depends(JWTBearer())):

    print("llego a get_current_user()")    
    print(token)
    print(token.get('email'))

    result = UsusarioServices(db).get_usuario_by_email(token.get('email'))
    
    dto: UsuarioDTO = jsonable_encoder(result)    
    print(dto)
    print("---------------")
    print(dto)
    
    #dto: UsuarioDTO = get_user_by_email2(token.get('email'))
    return True



@router.get("/prueba")
def prueba_ger_user(algo:str, current_user: Annotated[Boolean, Depends(token_validate)]):
    print("llego al back") 
    #get_user_by_email(email, db)
